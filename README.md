Syncpacks CookieCutter
========================

A cookiecutter template for integration services syncpacks

[cookiecutter](https://github.com/audreyr/cookiecutter)

Using CookieCutter for your project
-----------------------------------

    $ pip install cookiecutter
    $ cookiecutter https://github.com/marchingphoenix/is_syncpack_cookiecutter.git --checkout sl-internal

You will be asked about basic information:
	author, url_project, syncpack_name, syncpack_friendly_name, syncpack_description, version and the requires_minimum_is_version which is the IS system version where the syncpack is going to be installed

Visual Studio Code
================================
The generated package includes VSCode configuration settings to improve the SyncPack development process.

DevContainer
------------
The generated package will contain a [Visual Studio Code DevContainer](https://code.visualstudio.com/docs/remote/containers)  
When you open the generated folder with VSCode you will get a prompt to open the workspace within the container.  
This Container contains a functional environment for developing and testing your SyncPack steps without the need of a PowerFlow system.

Tasks
-----
The generated package will contain a [task](https://code.visualstudio.com/docs/editor/tasks) to build and upload your SyncPack to a PowerFlow system.

Usage:
1. Open the Command Pallet
1. Run `Tasks: Run Task`
1. Choose `PF: Build and Upload SyncPack`
1. Input your PF Hostname or IP
1. Input your PF Username (default: isadmin)
1. Input your PF Password (default: isadmin)

SyncPack should now be available to install on your PowerFlow system.

Settings
--------
The generated package will contain a `settings.json` to enable `pytest` and configure test discovery.