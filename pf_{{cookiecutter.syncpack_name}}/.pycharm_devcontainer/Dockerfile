FROM  {{ 'registry.scilo.tools/sciencelogic' if cookiecutter.dev_container_source == 'SL External' else 'registry.scilo.tools/internal' }}/pf-syncpack-devcontainer:{{cookiecutter.dev_container_version}}
WORKDIR /workspaces/pf_{{cookiecutter.syncpack_name}}
COPY . /workspaces/pf_{{cookiecutter.syncpack_name}}/
ENV PIP_CONFIG_FILE /workspaces/pf_{{cookiecutter.syncpack_name}}/.devcontainer/pip.conf
USER root
RUN pip3 install -f  /workspaces/pf_{{cookiecutter.syncpack_name}}/.offline_dependencies --disable-pip-version-check --no-warn-script-location -e .
USER 1001
