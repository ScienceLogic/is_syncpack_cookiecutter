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

**Usage**
1. After completing the cookie cutter run, open the generated folder in Visual Studio Code
1. Open a new Terminal in VSCode (ctrl+shift+`)
1. `cd` to `.devcontainer`
1. Run `docker build --pull --rm --network=host -f "Dockerfile" -t syncpack-env:latest .`
1. After the build completes, pull up the command pallet (ctrl+shift+P) and run `Remote-Containers: Reopen in Container`
Your environemt should now be ready.
If you need any additional syncpacks or packages to be available, add them to the .devcontainers/dev-requirements.txt, repeat the build command and re-open in the container again.

*Linux Notes*  
If the build fails to resolve the internal repositories, you may need to set `DOCKER_OPTS="--dns <dns ip>"` in `/etc/default/docker` and restart the docker service.

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