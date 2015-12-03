from threading import Thread
import time

__author__ = 'bardia'


class Simulator(Thread):
    def __init__(self, processor, delay):
        super(Simulator, self).__init__()
        self.processor = processor
        self.delay = delay * 1000
        self.still_continue = False

    def run(self):
        while self.still_continue:
            time.sleep(self.delay)
            self.processor.clock()

    def finish_signal(self):
        self.still_continue = False
