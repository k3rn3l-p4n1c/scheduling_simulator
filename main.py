from models.process import Process
from scheduler.fifo_scheduler import FIFOScheduler
from scheduler.sjf_scheduler import SJFScheduler
from gantt.chart import Drawer

__author__ = 'bardia'

# -*- coding: utf-8 -*-


if __name__ == '__main__':
    log = []
    scheduler = SJFScheduler()
    scheduler.add(Process(5))
    scheduler.add(Process(4))
    log.append((scheduler.get(), scheduler.time))
    scheduler.add(Process(1))
    log.append((scheduler.get(), scheduler.time))
    scheduler.add(Process(2))

    p = scheduler.get()
    log.append((p, scheduler.time))
    while p is not None:
        p = scheduler.get()
        log.append((p, scheduler.time))
    print log
    Drawer(log).draw()
