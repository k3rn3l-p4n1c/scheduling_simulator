from scheduler.asbtract_scheduler import AbstractScheduler

__author__ = 'bardia'


class LIFOScheduler(AbstractScheduler):
    """
    Using first in first out algorithm
    """

    def get(self):
        super(LIFOScheduler, self).get()
        if len(self.process_list) == 0:
            return None
        last_job = self.process_list[-1]

        return last_job

    def remove(self, process):
        self.process_list.remove(process)
