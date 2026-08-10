Syncpacks CookieCutter
========================

A cookiecutter template for integration services syncpacks

[cookiecutter](https://github.com/audreyr/cookiecutter)

Using CookieCutter for your project
-----------------------------------

    $ pip install cookiecutter
    $ cookiecutter https://github.com/ScienceLogic/is_syncpack_cookiecutter.git

You will be asked about basic information:
| Prompt | Description |
| --- | --- |
| author | Creator of the SyncPack |
| url_project | Link to the SyncPack Source Code |
| syncpack_name | Name of the SyncPack Module |
| syncpack_friendly_name | Display Name of the SyncPack |
| syncpack_description | What does this SyncPack do? |
| version | Initial SyncPack Version |
| requires_minimum_pf_version | Which version(s) of PowerFlow will this SyncPack support? |
| dev_container_source | Use SL External if you are not a ScienceLogic employee |
| dev_container_version | dev_container_version image version. i.e. for PF 2.4.1, the version should be 2.4.1 |
| include_mcp_components | Boolean determining to include MCP functionality |

Visual Studio Code
================================
The generated package includes VSCode configuration settings to improve the SyncPack development process.

DevContainer
------------
The generated package will contain a [Visual Studio Code DevContainer](https://code.visualstudio.com/docs/remote/containers)  
When you open the generated folder with VSCode you will get a prompt to open the workspace within the container.  
This PowerFlow Syncpack SDK(DevContainer) contains a functional environment for developing and testing your SyncPack steps without the need of a full PowerFlow system.

**Usage**
1. After completing the cookie cutter run, open the generated folder in Visual Studio Code
1. The .devcontainer folder should be detected and you should be prompted to re-open the workspace in the container. Click Yes.

If you are not prompted or you miss it, Open the command pallet (ctrl+shift+P) and run `Remote-Containers: Reopen in Container`

Your environemt should now be ready.
If you need any additional syncpacks or packages to be available, simply `pip install` them into your container. Remember to add them to your dependancies!

Tasks
-----
The generated workspace contains a number of [tasks](https://code.visualstudio.com/docs/editor/tasks) to assist with development.

### Build and upload your SyncPack to a PowerFlow system.

Usage:
1. Open the Command Pallet
1. Run `Tasks: Run Task`
1. Choose `PF: Build and Upload SyncPack`
1. Input your PF Hostname or IP
1. Input your PF Username (default: isadmin)
1. Input your PF Password (default: isadmin)

SyncPack should now be available to install on your PowerFlow system.

### Pre-Commit: Initialize
Initializes the pre-commit workflow. Run this after you have added a git repository to your workspace.

Usage:
1. Open the Command Pallet
1. Run `Tasks: Run Task`
1. Choose `Pre-Commit: Initialize`

Pre-Commit should now be ready to use.

### Pre-Commit: Run All Files
Manually run all Pre-Commit checks.

Usage:
1. Open the Command Pallet
1. Run `Tasks: Run Task`
1. Choose `Pre-Commit: Run All Files`

### Pre-Commit: auto-update
Check pre-commit tasts for workflow updates and update them if needed.

Usage:
1. Open the Command Pallet
1. Run `Tasks: Run Task`
1. Choose `Pre-Commit: auto-update`

### PF: Install SP - Offline Dependencies
Allows to install the current syncpack using offline dependencies.

Usage:
1. Open the Command Pallet
1. Run `Tasks: Run Task`
1. Choose `PF: Install SP - Offline Dependencies`
1. Input a Workspace Directory to read offline dependencies (default: ${workspaceFolder}/.offline_dependencies)

### PF: Install SP - Dependencies from PF(devpi)
Allows to install the current syncpack using a remote PF system.

Usage:
1. Open the Command Pallet
1. Run `Tasks: Run Task`
1. Choose `PF: Install SP - Dependencies from PF(devpi)`
1. Input a Workspace Directory to read offline dependencies (default: ${workspaceFolder}/.offline_dependencies)
1. Input your PF Hostname or IP
1. Input your PF Username (default: isadmin)
1. Input your PF Password (default: isadmin)

### PF: Install SP - Dependencies from PF(devpi) + Offline dependencies
Allows to install the current syncpack using a remote PF system and offline dependencies.

Usage:
1. Open the Command Pallet
1. Run `Tasks: Run Task`
1. Choose `PF: Install SP - Dependencies from PF(devpi) + Offline dependencies`
1. Input a Workspace Directory to read offline dependencies (default: ${workspaceFolder}/.offline_dependencies)
1. Input your PF Hostname or IP
1. Input your PF Username (default: isadmin)
1. Input your PF Password (default: isadmin)

Snippets
-----
### PF Apps Snippet
The PFApp.code-snippets snippet allows to quickly have a basic application structure.
Usage:
1. Create a json file with the corresponding application name in the apps folder
2. In the file write **pfapp** and when vscode suggests the expected snippet to use, press Enter
3. The cursor will be positioned in the property that needs to be edited
4. Press Tab to go the next property to edit

### PF Step Snippet
The PFStep.code-snippets snippet allows to quickly have a basic step structure.

Usage:
1. Create a python file with the corresponding step name in the steps folder
2. In the file start writing **pfstep** and when vscode suggests the expected snippet to use, press Enter
3. The cursor will be positioned in the property that needs to be edited
4. Press Tab to go the next property to edit

### PF Step Test Snippet
The PFStepTest.code-snippets snippet allows to quickly have a basic step structure.

Usage:
1. Create a python file with the corresponding step test name in the tests/steps folder
2. In the file start writing **pfsteptest** and when vscode suggests the expected snippet to use, press Enter
3. The cursor will be positioned in the property that needs to be edited
4. Press Tab to go the next property to edit

More details on how to use and create snippets in [VSCode official documentation](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

Settings
--------
The generated package will contain a `settings.json` to enable `pytest` and configure test discovery.

PyCharm
================================
The generated package includes PyCharm configuration settings to improve the SyncPack development process.

**Usage**
1. After completing the cookie cutter run, open the generated folder in PyCharm.
   1. When working with more than 1 syncpack repository, it is recommended to open the root directory in which the needed repositories are located.
2. The .pycharm_devcontainer folder contains files to configure a Docker Python Interpreter in PyCharm
3. Mark the syncpack directory as Source. Using Right Click > Mark Directory as > Sources Root
4. Configure the docker-compose.yml file located in .pycharm_devcontainer/docker-compose.yml as a Docker Compose Remote Python interpreter. Follow the instruction in [PyCharm official documentation](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote).
5. Select the interpreter created in the step 4 as default for your workspace
6. Your environment should now be ready


Model Context Protocol (MCP) 
================================

The cookiecutter includes support for embedding MCP components within SyncPacks to enhance AI-powered development workflows.

## SAMCP Components Directory Structure

```
samcp_components/
├── apps/
│   └── dummy_app.py
├── prompts/
│   └── prompts.py
├── resources/
│   └── resources.py
├── templates/
│   └── templates.py
└── tools/
    └── tools.py
```

The `samcp_components` directory provides a standardized framework for building modular, reusable components within your SyncPack.

**Prompts** (`prompts/prompts.py`)
- Extend `BasePrompt` for handling user interactions and input processing
- Example: `DummyPrompt` class with `dummy_function(name: str)` for placeholder text generation
- Used for creating interactive elements and generating dynamic prompts for AI interactions

**Resources** (`resources/resources.py`)
- Extend `BaseResource` for managing data sources and external resources
- Example: `DummyResource` class with `dummy_function()` returning static data
- Used for providing read-only access to data that AI models can reference (databases, files, APIs, documentation)

**Templates** (`templates/templates.py`)
- Extend `BaseTemplate` for generating formatted output and content
- Example: `DummyTemplate` class with `dummy_function(name: str)` for content generation
- Used for creating structured output formats and reusable content templates

**Tools** (`tools/tools.py`)
- Extend `BaseTool` for executing specific operations and utilities
- Example: `DummyTool` class with `dummy_function(name: str, config: str)` returning configuration data
- Used for performing actions that modify state or execute operations (create files, send emails, run commands)

**Apps** (`apps/dummy_app.py`)
- A `FastMCPApp` subclass (from `fastmcp.apps.app`) placed under `samcp_components/apps/`. Unlike Tools/Resources/Prompts/Templates (which set `self.prefix`), an app is a live provider: it registers one or more model-visible entry points via `@self.ui(...)`, each returning a `prefab_ui` `PrefabApp` UI that is rendered in UI-capable MCP clients.
- Example: `DummyApp` with a single `dummy_app(name: str)` entry point returning a placeholder `PrefabApp` view.
- Requires the `fastmcp-slim[apps]` extra (prefab-ui), which is present in the SAMCP dev container / image but is not resolvable on a bare host.
- The stub imports **only** `fastmcp` and `prefab_ui` — it must never import `base_steps_syncpack` or any sibling syncpack, since the generated syncpack cannot assume base_steps is installed. For an example of the more advanced pattern (app-only backend tools the UI invokes that stay hidden from the model, plus the FastMCP 3.4.x registration workaround), read `base_steps_syncpack/samcp_components/apps/syncpack_setup.py` for guidance only — do not import from it.

**How sa_mcp discovers apps:** sa_mcp's component manager scans `{syncpack}/samcp_components/apps/*.py` (skipping `__init__.py`), finds classes that subclass `FastMCPApp`, are not `FastMCPApp` itself, and are **defined in that module** (imported subclasses are ignored, so importing `FastMCPApp` at the top of the stub does not cause double-registration). Each match is instantiated with no args and registered as a real `FastMCPApp` provider — not flattened into tools/resources/prompts.

All components include dummy implementations as starting points that should be customized for your specific use case.