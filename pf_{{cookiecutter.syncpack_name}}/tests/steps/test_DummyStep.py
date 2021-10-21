import pytest
from conftest import SYNCPACK


@pytest.mark.parametrize(
    "stepdict,outdata",
    [
        (
            {
                "name": "DummyStep",
                "file": "DummyStep",
                "syncpack": SYNCPACK,
                "snow_hostname": "pytest.servicenow.com",
            },
            "foo"
        )
    ],
)
def test_ProcessEventTrigger(stepdict, outdata, syncpack_step_runner):
    processed_data = syncpack_step_runner.run(stepdict)
    assert processed_data == outdata