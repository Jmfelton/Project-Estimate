from .estimate import Estimate


class Task(object):
    def __init__(self, estimate: Estimate = None, name=None):
        self._name = name
        if estimate is None:
            self._estimate = Estimate()
        else:
            self._estimate = estimate

    def __str__(self):
        return "{}: \n Estimated Time (in Days): {} \n complications may make task take {} or {} days." \
            .format(self._name, self.estimated_duration,
                    self.get_duration_with_num_std_deviations(1),
                    self.get_duration_with_num_std_deviations(2))

    def get_name(self):
        return self._name

    def set_name(self, task_name: str):
        self._name = task_name

    def set_estimate(self, estimate: Estimate):
        self._estimate = estimate

    @property
    def estimated_duration(self):
        return self._estimate.expected_duration

    def get_duration_with_num_std_deviations(self, num_deviations: int):
        return self.estimated_duration + (num_deviations * self.standard_deviation)

    @property
    def standard_deviation(self):
        return self._estimate.standard_deviation_of_duration
