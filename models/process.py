__author__ = 'bardia'


class Process(object):
    count = 1

    def __init__(self, execution_time):
        self.index = Process.count
        self.arrival = None
        self.execution = execution_time
        self.remaining = execution_time

        Process.count += 1

    def __str__(self):
        return '({}, arrival={}, execution={}, remaining={})'.format(self.index, self.arrival, self.execution,
                                                                     self.remaining)
