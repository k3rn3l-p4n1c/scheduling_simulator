from asbtract_scheduler import AbstractScheduler

__author__ = 'bardia'


class SJFScheduler(AbstractScheduler):
    """
    Using Short job first algorithm for scheduling
    """

    def get(self):
        super(SJFScheduler, self).get()
        if len(self.process_list) == 0:
            return None
        short_job = self.process_list[0]
        short_job.remaining -= 1
        if short_job.remaining == 0:
            self.process_list.remove(short_job)
            self.process_list.sort(key=lambda x: x.execution)
        return short_job
