"""DummyApp — a minimal FastMCPApp guided-UI stub.

Demonstrates the syncpack app discovery contract: place a FastMCPApp subclass
under ``samcp_components/apps/`` and the SAMCP server (sa_mcp) discovers it in
the syncpack virtualenv, instantiates it with no args, and registers it as a
live ``FastMCPApp`` provider. Only classes DEFINED in this module are
discovered, so importing ``FastMCPApp`` here does not cause double-registration.

This is distinct from the PowerFlow workflow apps under the package's ``apps/``
directory (JSON step-sequence definitions) — those are unrelated to MCP.

One model-visible entry point (``dummy_app``) returns a PrefabApp view. For an
example of the more advanced pattern — app-only backend tools the UI can call
that stay hidden from the model, plus the FastMCP 3.4.x registration workaround
— see the base_steps_syncpack ``samcp_components/apps/syncpack_setup.py``
reference implementation. That is an example to read for guidance only; do NOT
import from base_steps_syncpack (it is not a dependency of your syncpack).

Requires ``fastmcp-slim[apps]`` (prefab-ui), present in the SAMCP dev
container / image but not resolvable on a bare host.
"""

from __future__ import annotations

from fastmcp.apps.app import FastMCPApp
from prefab_ui.app import PrefabApp
from prefab_ui.components import Card, CardContent, CardHeader, Column, H3, Muted


class DummyApp(FastMCPApp):
    """Minimal guided-setup app stub shipped under samcp_components/apps/."""

    def __init__(self) -> None:
        super().__init__("DummyApp")
        self._register()

    def _register(self) -> None:
        @self.ui(
            name="dummy_app",
            description=(
                "Open a placeholder guided-setup UI. Replace this with your "
                "syncpack's own setup flow."
            ),
        )
        def dummy_app(name: str) -> PrefabApp:
            """Render the placeholder UI.

            Args:
                name: A placeholder input echoed into the view.
            """
            with Card(css_class="max-w-lg mx-auto") as view:
                with CardHeader():
                    H3("Dummy syncpack app")
                with CardContent(), Column(gap=2):
                    Muted(
                        f"This is a placeholder FastMCPApp for '{name}'. Replace "
                        f"it with your syncpack's guided-setup UI."
                    )
            return PrefabApp(view=view, state={})
