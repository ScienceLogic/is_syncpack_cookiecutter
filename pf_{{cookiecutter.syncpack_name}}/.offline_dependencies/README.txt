# Install offline dependencies into the devcontainer

1. Copy all the needed wheels(including SL Syncpacks) files into this .offline_dependencies directory
2. Add the corresponding dependencies a syncpack needs to the 'requires_dist' property in the meta.json file
3. Once the devcontainer is up and running, run one of the vscode tasks to install a syncpack using offline dependencies. i.e. 'PF: Install SP - Offline Dependencies'
