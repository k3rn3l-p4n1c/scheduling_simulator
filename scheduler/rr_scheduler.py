from asbtract_scheduler import AbstractScheduler

__author__ = 'bardia'


class RRScheduler(AbstractScheduler):
    """
    Using round robin algorithm for scheduling
    """
    def __init__(self):
        super(RRScheduler, self).__init__()
        self.iterator = 0

    def get(self):
        super(RRScheduler, self).get()
        if len(self.process_list) == 0:
            return None

        self.iterator += 1
        if self.iterator >= len(self.process_list):
            self.iterator = 0

        job = self.process_list[self.iterator]

        return job

    def remove(self, process):
        self.process_list.remove(process)
