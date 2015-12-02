__author__ = 'bardia'


class Process(object):
    count = 0

    def __init__(self, arrival_time, execution_time):
        self.index = Process.count
        self.arrival = arrival_time
        self.execution = execution_time
