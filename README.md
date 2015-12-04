# scheduling_simulator
Scheduling process simulator for learning purpose

This project is a simulator for scheduling process like a operating system kernel for understand the behavior of each scheduling algorithm.

## How to install (Linux)

1- Install python and virtualenv and pip
```
$ sudo apt-get install python python-pip python-virtualenv
```

2- Download and extract or clone the project
3- In terminal go to project directory
4- Create a virtual environment
```
$ virtualenv venv
```
5- Change the source of environment to created one
```
$ source venv/bin/activate
```
6- Install requirments
```
$ pip install requirments -r
```

## How to run project
1- Go to project directory and run
```
$ python main.py
```
2- Insert number of algorithm you want for scheduling
3- Insert delay time as the lenght of an atomic run
4- Insert execution time of process to create them real time.
5- Inser 0 to finish. Do not finish program before the buffer is empty.

## Scheduling algorithms
    1- First come first serve
    2- First in first out
    3- Last in first out
    4- Round Robin
    5- Short job first
    6- Shortest remaining time

## Todo
1- Graphical user interface
2- Fast mode. Read arrival time and execution time from file and no delay for simulation.
