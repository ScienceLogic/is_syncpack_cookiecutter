import os
from importlib import import_module

import pytest

import {{cookiecutter.syncpack_name}}
from ipaascommon.json_utils import get_dict_from_ex_json_str
from ipaascore.BaseStep import BaseStep


def get_obj_from_module(object_name, module):
    try:
        return getattr(import_module(module), object_name)
    except (AttributeError, ModuleNotFoundError):
        return None


@pytest.fixture(
    params=os.listdir(os.path.join({{cookiecutter.syncpack_name}}.__path__[0], "apps"))
)
def app_name(request):
    return request.param


def test_json_app(app_name):
    app_path = os.path.join(
        {{cookiecutter.syncpack_name}}.__path__[0], "apps", app_name
    )
    app_json = None
    assert os.path.isfile(app_path)
    with open(app_path) as file_app:
        json_string = file_app.read()
        app_json = get_dict_from_ex_json_str(json_string)

    assert isinstance(app_json, dict), "App definition must be a dictionary"
    assert "steps" in app_json.keys(), "steps key must be present"
    assert type(app_json["steps"]) is list, "the value of steps must be a list"
    assert len(app_json["steps"]) > 0, "you must have at least one step"

    for step in app_json["steps"]:
        assert "name" in step.keys(), "name key must be present in step definition"
        assert step["name"], "name must have a value"
        assert "file" in step.keys(), "file key must be present in step definition"
        assert step["file"], "file key must have a value"
        assert (
            "syncpack" in step.keys()
        ), "syncpack key must be present in step definition"
        assert step["syncpack"], "syncpack key must have a value"
        step_object = get_obj_from_module(
            step["file"], f'{step["syncpack"]}.steps.{step["file"]}'
        )
        assert (
            step_object
        ), f"Step {step['file']} was not found in SyncPack: {step['syncpack']}"
        assert isinstance(
            step_object(), BaseStep
        ), f"Step {step['file']} must be a subclass of BaseStep"

    assert (
        "app_variables" in app_json.keys() and type(app_json["app_variables"]) is list
    ), "app_variables key must be present and its value must be a list"
