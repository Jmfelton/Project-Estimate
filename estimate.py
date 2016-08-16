class Estimate(object):
    """Probability Distribution of Project Estimate Times"""

    def __init__(self, o=0, n=0, p=0):
        self._optimistic_estimate = o
        self._nominal_estimate = n
        self._pessimistic_estimate = p

    @property
    def optimistic_estimate(self):
        return self._optimistic_estimate

    @optimistic_estimate.setter
    def optimistic_estimate(self, o):
        self._optimistic_estimate = o

    @property
    def nominal_estimate(self):
        return self._nominal_estimate

    @nominal_estimate.setter
    def nominal_estimate(self, n):
        self._nominal_estimate = n

    @property
    def pessimistic_estimate(self):
        return self._pessimistic_estimate

    @pessimistic_estimate.setter
    def pessimistic_estimate(self, p):
        self._pessimistic_estimate = p

    @property
    def standard_deviation_of_duration(self):
        """Return standard deviation of Estimate in days"""
        standard_deviation = (self._pessimistic_estimate - self._optimistic_estimate) / 6
        return round(standard_deviation, 1)

    @property
    def expected_duration(self):
        """Return expected duration of Estimate in days"""
        distribution = (self._optimistic_estimate + (4 * self._nominal_estimate) + self.pessimistic_estimate) / 6
        return round(distribution, 1)
