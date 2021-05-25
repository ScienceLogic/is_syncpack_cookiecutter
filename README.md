Syncpacks CookieCutter
========================

A cookiecutter template for integration services syncpacks

[cookiecutter](https://github.com/audreyr/cookiecutter)

Using CookieCutter for your project
-----------------------------------

    $ pip install cookiecutter
    $ cookiecutter https://github.com/ScienceLogic/is_syncpack_cookiecutter.git

You will be asked about basic information:
	author, url_project, syncpack_name, syncpack_friendly_name, syncpack_description, version and the requires_minimum_is_version which is the IS system version where the syncpack is going to be installed

Visual Studio Code
================================
The generated package includes VSCode configuration settings to improve the SyncPack development process.

DevContainer
------------
The generated package will contain a [Visual Studio Code DevContainer](https://code.visualstudio.com/docs/remote/containers)  
When you open the generated folder with VSCode you will get a prompt to open the workspace within the container.  
This Container contains a functional environment for developing and testing your SyncPack steps without the need of a full PowerFlow system.

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


Settings
--------
The generated package will contain a `settings.json` to enable `pytest` and configure test discovery.