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
        first_job.remaining -= 1
        if first_job.remaining == 0:
            self.process_list.remove(first_job)
        return first_job
