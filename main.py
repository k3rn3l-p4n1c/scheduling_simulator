from models.process import Process
from scheduler.fifo_scheduler import FIFOScheduler
from scheduler.sjf_scheduler import SJFScheduler

__author__ = 'bardia'

# -*- coding: utf-8 -*-


if __name__ == '__main__':
    scheduler = FIFOScheduler()
    scheduler.add(Process(5))
    scheduler.add(Process(4))
    print scheduler.get()
    scheduler.add(Process(1))
    print scheduler.get()
    scheduler.add(Process(2))

    p = scheduler.get()
    print p
    while p is not None:
        p = scheduler.get()
        print p
