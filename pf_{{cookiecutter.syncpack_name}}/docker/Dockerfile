FROM scr.sl1.io/is-worker:dev AS test

WORKDIR /workspace
COPY . /workspace

RUN apt-get update && \
apt-get install -y python3 python3-dev && \
python setup.py sdist bdist_wheel && \
pip install tox
