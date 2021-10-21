import os
import pytest
import {{cookiecutter.syncpack_name}}
from ipaascommon.json_utils import get_dict_from_ex_json_str


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

    assert isinstance(app_json, dict)
    assert "steps" in app_json.keys()
    assert type(app_json["steps"]) is list
    assert len(app_json["steps"]) > 0

    for step in app_json["steps"]:
        assert "name" in step.keys()
        assert step["name"]
        assert "file" in step.keys()
        assert step["file"]
        assert "syncpack" in step.keys()
        assert step["syncpack"]

    assert (
        "app_variables" in app_json.keys() and type(app_json["app_variables"]) is list
    )
