__author__ = 'bardia'


class AbstractScheduler(object):
    def __init__(self):
        self.time = 0
        self.process_list = []

    def add(self, process):
        process.arrival = self.time

        self.process_list.append(process)

    def get(self):
        self.time += 1
