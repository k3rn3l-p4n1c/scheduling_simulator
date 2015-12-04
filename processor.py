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
            proc.arrival = self.time
            self.scheduler.add(proc)
        self.incoming_process_buffer = []

        proc = self.scheduler.get()

        if proc is None:
            print 'pulse {} IDLE | in line: {}'.format(self.time, len(self.scheduler.process_list))
        else:
            print 'pulse {} run p{} | in line: {}'.format(self.time, proc.index, len(self.scheduler.process_list))

        if proc is not None:
            proc.run(self.time)

            if proc.finished():
                self.scheduler.remove(proc)

        self.log.append((proc, self.time))
