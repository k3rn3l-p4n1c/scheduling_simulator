from scheduler.asbtract_scheduler import AbstractScheduler

__author__ = 'bardia'


class FIFOScheduler(AbstractScheduler):
    """
    Using first in first out algorithm
    """

    def get(self):
        super(FIFOScheduler, self).get()
        if len(self.process_list) == 0:
            return None
        first_job = self.process_list[0]

        return first_job

    def remove(self, process):
        self.process_list.remove(process)