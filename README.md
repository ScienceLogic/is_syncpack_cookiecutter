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