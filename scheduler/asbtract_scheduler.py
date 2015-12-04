__author__ = 'bardia'


class AbstractScheduler(object):
    def __init__(self):
        self.process_list = []

    def add(self, process):
        self.process_list.append(process)

    def get(self):
        pass
