__author__ = 'bardia'


class Process(object):
    count = 1

    def __init__(self, execution_time):
        self.index = Process.count
        self.execution = execution_time
        self.remaining = execution_time

        self.wait = 0
        self.finish_time = None
        self.turn_around = None
        self.first_run = None
        self.arrival = None
        self.response_time = None
        self.turn_around = None

        Process.count += 1

    def run(self, time):
        self.remaining -= 1
        if self.first_run is None:
            self.first_run = time
            self.response_time = self.first_run - self.arrival

        if self.remaining == 0:
            self.finish_time = time
            self.wait = self.finish_time - self.execution - self.arrival
            self.turn_around = self.finish_time - self.arrival

    def finished(self):
        return self.remaining <= 0

    def __str__(self):
        return '({}, arrival={}, execution={}, remaining={})'.format(self.index, self.arrival, self.execution,
                                                                     self.remaining)
