__author__ = 'bardia'


class Processor(object):

    def __init__(self, scheduler):
        self.time = 0
        self.incoming_process_buffer = []
        self.scheduler = scheduler
        self.log = []

    def add(self, process):
        self.incoming_process_buffer.append(process)

    def clock(self):
        self.time += 1

        for proc in self.incoming_process_buffer:
            self.scheduler.add(proc)
        self.incoming_process_buffer = []

        proc = self.scheduler.get()

        proc.run()

        self.log.append((proc, self.time))
