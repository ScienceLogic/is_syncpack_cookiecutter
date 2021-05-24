# Update the VARIANT arg in devcontainer.json to pick a Python version: 3, 3.8, 3.7, 3.6 
ARG VARIANT=3
FROM python:3.7-stretch

# Options for common setup script
ARG INSTALL_ZSH="true"
ARG UPGRADE_PACKAGES="true"
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
COPY library-scripts/*.sh /tmp/library-scripts/
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    # Remove imagemagick due to https://security-tracker.debian.org/tracker/CVE-2019-10131
    && apt-get purge -y imagemagick imagemagick-6-common \
    # Install common packages, non-root user
    && /bin/bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" \
    # Clean up
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts

# Setup default python tools in a venv via pipx to avoid conflicts
ARG DEFAULT_UTILS="\
    pylint \
    flake8 \
    autopep8 \
    black \
    yapf \
    mypy \
    pydocstyle \
    pycodestyle \
    bandit \
    virtualenv"
ENV PIPX_HOME=/usr/local/py-utils
ENV PIPX_BIN_DIR=${PIPX_HOME}/bin
ENV PATH=${PATH}:${PIPX_BIN_DIR}
RUN mkdir -p ${PIPX_BIN_DIR} \
    && export PYTHONUSERBASE=/tmp/pip-tmp \
    && pip3 install --disable-pip-version-check --no-warn-script-location --no-cache-dir --user pipx \
    && /tmp/pip-tmp/bin/pipx install --pip-args=--no-cache-dir pipx \
    && echo "${DEFAULT_UTILS}" | xargs -n 1 /tmp/pip-tmp/bin/pipx install --system-site-packages --pip-args=--no-cache-dir --pip-args=--force-reinstall \
    && chown -R ${USER_UID}:${USER_GID} ${PIPX_HOME} \
    && rm -rf /tmp/pip-tmp


# [Optional] Uncomment this section to install additional packages.
#
RUN wget http://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-6-amd64.deb && \
    dpkg -i couchbase-release-1.0-6-amd64.deb && apt-get update && \
    export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends libcouchbase-dev && \
    rm couchbase-release-1.0-6-amd64.deb
 
# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY dev-requirements.txt /tmp/pip-tmp/
RUN pip3 install --upgrade pip~=20.2.3 \
    && pip3 --disable-pip-version-check --no-cache-dir install --extra-index-url http://scr.sl1.io/artifactory/api/pypi/pypi-local/simple  --trusted-host scr.sl1.io -r /tmp/pip-tmp/dev-requirements.txt \
    && pip3 --disable-pip-version-check --no-cache-dir install --extra-index-url http://scr.sl1.io/artifactory/api/pypi/pypi-local/simple  --trusted-host scr.sl1.io --no-deps pytest-powerflow iscli \
    && rm -rf /tmp/pip-tmp