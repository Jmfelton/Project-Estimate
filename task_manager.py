from .Task import Task
from math import sqrt


class TaskManager(object):
    def __init__(self, name=None, tasks=None, task=None):
        self._name = name
        if tasks is not None:
            self.tasks = tasks
        else:
            self.tasks = []
        if task is not None:
            self.tasks.append(task)

    def get_name(self):
        return self._name

    def set_name(self, task_name):
        self._name = task_name

    def add_task(self, task: Task):
        self.tasks.append(task)

    @property
    def distribution_all_tasks(self):
        distribution = sum(task.estimated_duration for task in self.tasks)
        assert isinstance(distribution, float)
        return distribution

    @property
    def std_deviation_all_tasks(self):
        assert self.tasks is not None
        std_deviation = 0
        for task in self.tasks:
            std_deviation += pow(task.standard_deviation, 2)
        total_std_deviation = sqrt(std_deviation)

        return round(total_std_deviation, 2)
