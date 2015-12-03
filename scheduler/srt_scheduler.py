from asbtract_scheduler import AbstractScheduler

__author__ = 'bardia'


class SRTScheduler(AbstractScheduler):
    """
    Using Short remaining time algorithm for scheduling
    """

    def get(self):
        super(SRTScheduler, self).get()
        if len(self.process_list) == 0:
            return None
        short_job = self.process_list[0]

        self.process_list.sort(key=lambda x: x.remaining)
        return short_job

    def remove(self, process):
        self.process_list.remove(process)
