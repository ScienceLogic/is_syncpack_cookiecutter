from ipaascore.BaseStep import BaseStep


class DummyStep(BaseStep):

    def __init__(self):
        pass

    def execute(self):
        """
        All logic main logic for executing the step happens here
        :return:
        """
        self.save_data_to_next_step("foo")
