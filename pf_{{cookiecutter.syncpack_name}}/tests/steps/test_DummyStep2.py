import pytest
from conftest import SYNCPACK


STEP_NAME = "DummyStep2"

test_data = [
    (
        {
            "name": STEP_NAME,
            "file": STEP_NAME,
            "syncpack": SYNCPACK,
            "dummy_step_parameter": "dummy_string",  # example of a step parameter
        },
        {},
        "foo",
    )
]


@pytest.mark.parametrize(
    "step_dict, in_data, out_data", test_data, ids=["first test"],
)
def test_DummyStep2(step_dict, in_data, out_data, syncpack_step_runner):
    # input data helps to simulate the data received from previous step(s)
    syncpack_step_runner.data_in = in_data
    data = syncpack_step_runner.run(step_dict)
    # output data represents the data saved for the next step using self.save_data_for_next_step("foo")
    assert data == out_data
