In general, the algorithm is basically:
1) sort the jobs in ascending order according to their finishing time
2) try to assign the job that finishes earlier first. if multiple machines are available, choose the one with smallest waiting time.
3) for multiple machines with the same waiting time, break ties arbitrarily


To run the code:
Name input file as input.txt
Run test.py ($ python3 test.py)

