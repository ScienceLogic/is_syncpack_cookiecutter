from ipaascore.BaseStep import BaseStep


class DummyStep2(BaseStep):

    def __init__(self):
        pass

    def execute(self):
        """
        All logic main logic for executing the step happens here
        :return:
        """
        # Get data from previous step
        prev_data = self.join_previous_step_data()
        self.logger.debug(f'prev_data: {prev_data}')

        # Save data for next step
        self.save_data_for_next_step(prev_data)
