from models.process import Process
from processor import Processor
from scheduler.fcfs_scheduler import FCFSScheduler
from scheduler.fifo_scheduler import FIFOScheduler
from scheduler.lifo_scheduler import LIFOScheduler
from scheduler.rr_scheduler import RRScheduler
from scheduler.sjf_scheduler import SJFScheduler
from gantt.chart import draw
from scheduler.srt_scheduler import SRTScheduler
from simulator import Simulator

__author__ = 'bardia'

# -*- coding: utf-8 -*-


if __name__ == '__main__':
    print "Scheduling simulator\n"
    print "Which of the scheduling algorithm you want?"
    print "\t 1- First come first serve"
    print "\t 2- First in first out"
    print "\t 3- Last in first out"
    print "\t 4- Round Robin"
    print "\t 5- Short job first"
    print "\t 6- Shortest remaining time"

    while True:
        choice = input("Enter number 1-6:")

        if choice == 1:
            cpu = Processor(FCFSScheduler())
        elif choice == 2:
            cpu = Processor(FIFOScheduler())
        elif choice == 3:
            cpu = Processor(LIFOScheduler())
        elif choice == 4:
            cpu = Processor(RRScheduler())
        elif choice == 5:
            cpu = Processor(SJFScheduler())
        elif choice == 6:
            cpu = Processor(SRTScheduler())
        else:
            print("Wrong input")
            continue
        break

    delay = input("Enter processor's delay for each clock (second):")

    simulator = Simulator(cpu, delay)

    print('Enter 0 to exit')
    print "Enter execution time of incoming process:"
    simulator.start()

    all_process = []

    while True:
        execution_time = input()
        if execution_time == 0:
            simulator.finish_signal()
            break
        process = Process(execution_time)
        cpu.add(process)
        all_process.append(process)

    print 'Average waiting time: {}'.format(sum([p.wait for p in all_process])/len(all_process))
    print 'Average response time: {}'.format(sum([p.response_time for p in all_process])/len(all_process))
    print 'Average turn around time: {}'.format(sum([p.turn_around for p in all_process])/len(all_process))
    draw(cpu.log)
