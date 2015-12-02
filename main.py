from models.process import Process
from scheduler.fifo_scheduler import FIFOScheduler
from scheduler.lifo_scheduler import LIFOScheduler
from scheduler.rr_scheduler import RRScheduler
from scheduler.sjf_scheduler import SJFScheduler
from gantt.chart import Drawer
from scheduler.srt_scheduler import SRTScheduler

__author__ = 'bardia'

# -*- coding: utf-8 -*-


if __name__ == '__main__':
    log = []
    scheduler = SRTScheduler()
    scheduler.add(Process(5))
    log.append((scheduler.get(), scheduler.time))
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
