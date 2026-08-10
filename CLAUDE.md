# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A [Cookiecutter](https://github.com/audreyr/cookiecutter) template that scaffolds PowerFlow SyncPack integration packages. Running the template generates a complete Python project with steps, apps, tests, DevContainer, pre-commit hooks, and optional MCP components.

## Generating a SyncPack

```bash
pip install cookiecutter
cookiecutter https://github.com/ScienceLogic/is_syncpack_cookiecutter.git
# or from a local checkout:
cookiecutter /path/to/is_syncpack_cookiecutter
```

Prompts and their meanings:

| Prompt | Notes |
|---|---|
| `syncpack_name` | Python module name — lowercase, no spaces (e.g. `my_integration`) |
| `dev_container_source` | Choose `SL External` if not a ScienceLogic employee |
| `dev_container_version` | Match the PowerFlow version you're targeting (e.g. `2.4.1`) |
| `include_mcp_components` | Defaults to `no`; choose `yes` to scaffold AI/MCP component stubs |

## Template Structure

```
is_syncpack_cookiecutter/
├── cookiecutter.json                        # Prompt definitions and defaults
├── hooks/post_gen_project.py               # Removes samcp_components/ when include_mcp_components=no
└── pf_{{cookiecutter.syncpack_name}}/      # The template that becomes the generated project
    ├── setup.py                            # Reads meta.json dynamically; no duplication
    ├── {{cookiecutter.syncpack_name}}/
    │   ├── meta.json                       # Single source of truth for name, version, author, deps, schedules
    │   ├── apps/                           # App JSON definitions
    │   ├── steps/                          # BaseStep subclasses
    │   ├── configs/                        # Configuration JSON files
    │   └── samcp_components/              # MCP stubs incl. apps/ (removed if not requested)
    └── tests/
        ├── conftest.py                     # Exposes SYNCPACK name; syncpack_step_runner fixture
        ├── test_app_files.py               # Validates all app JSONs and step imports
        └── steps/                          # Per-step parameterized tests
```

## Testing the Template Itself

There is no test suite for the cookiecutter template itself. To verify changes, generate a project locally and run its tests:

```bash
cookiecutter . --no-input   # generates with defaults from cookiecutter.json
cd pf_syncpack_test
pip install -e .
pytest -v tests/
```

## Generated Project: Key Patterns

### Steps

All steps inherit from `BaseStep` and implement `execute()`:

```python
class MyStep(BaseStep):
    def __init__(self):
        pass

    def execute(self):
        prev = self.join_previous_step_data()   # receive data from upstream step
        self.save_data_for_next_step(result)    # pass data to downstream step
```

### App JSON

Apps wire steps together. Each step entry must have `name`, `file` (class name), and `syncpack` (module name). `output_to` routes output to the next step by name.

```json
{
  "steps": [
    {"name": "Step A", "file": "StepA", "syncpack": "my_syncpack", "output_to": ["Step B"]},
    {"name": "Step B", "file": "StepB", "syncpack": "my_syncpack"}
  ],
  "app_variables": []
}
```

`test_app_files.py` validates every `.json` in `apps/` — it checks structure and dynamically imports each step class to confirm it is a `BaseStep` subclass.

### meta.json

`setup.py` reads `meta.json` at build time — update only `meta.json` for name, version, author, dependencies, and schedule definitions. Never edit `setup.py` for these fields.

### Step Tests

Tests use a `syncpack_step_runner` fixture and are parameterized with `(step_dict, in_data, out_data)` tuples:

```python
@pytest.mark.parametrize("step_dict, in_data, out_data", test_data)
def test_MyStep(step_dict, in_data, out_data, syncpack_step_runner):
    syncpack_step_runner.data_in = in_data
    data = syncpack_step_runner.run(step_dict)
    assert data == out_data
```

### MCP Components

When `include_mcp_components=yes`, stubs are generated under `samcp_components/{tools,resources,prompts,templates}/`. Each class extends the appropriate MCP base class and must set `self.prefix` to the syncpack name for correct namespacing in the MCP server.

```python
class MyTool(BaseTool):
    def __init__(self):
        super().__init__(name="my_tool", description="...", tags=[...])
        self.function_tool = self.my_function
        self.prefix = SYNCPACK   # must be set — controls MCP registered name
```

The `SYNCPACK` constant at the top of each stub file is a placeholder — replace it with the actual syncpack name.

When `include_mcp_components=yes`, an `apps/` stub is also generated: `apps/dummy_app.py`, class `DummyApp` — a self-contained `FastMCPApp` subclass (from `fastmcp.apps.app`) with one `@self.ui` entry point returning a `prefab_ui` `PrefabApp`. sa_mcp discovers it (scanning `samcp_components/apps/*.py` for locally-defined `FastMCPApp` subclasses) and registers it as a live provider, not flattened into tools/resources/prompts. This is unrelated to the workflow `apps/*.json` step-sequence definitions elsewhere in the package. Unlike the other stubs, the app has no `self.prefix`/`SYNCPACK` namespacing. The stub imports only `fastmcp` + `prefab_ui` and must never import `base_steps_syncpack` — the generated syncpack cannot assume base_steps is installed.

## Generated Project: Commands

```bash
# Install
pip install -e .

# Test
pytest -v tests/
pytest -v tests/steps/test_MyStep.py          # single file
pytest -v tests/steps/test_MyStep.py::test_fn # single test

# Lint / format
pre-commit run --all-files   # black + flake8 + pytest + JSON validation
pre-commit install            # wire hooks after git init

# Build and deploy to PowerFlow
python setup.py sdist bdist_wheel
iscli -H <host> -U <user> -p <pass> -ukFf .
```

## Modifying the Template

- Jinja2 syntax (`{{cookiecutter.variable}}`) is used throughout Python files, JSON, and directory names. Test changes by generating a project with `cookiecutter . --no-input`.
- `hooks/post_gen_project.py` runs after generation. It only removes `samcp_components/` — keep any new conditional logic here rather than adding complex branching in template files.
- `cookiecutter.json` controls prompt order and defaults. The first item in a list is the default selection (e.g., `include_mcp_components` defaults to `"no"`).
