import ReadInput
import Job
# Schedule has attributes:
# Machine are all the machines
# JobNotDone will includes any jobs that can not be schedule due to time conflict
# with all the machines in Machines
# Jobs are the untouched jobs in job list
class Schedule(object):
    def __init__(self, MachineNumber, JobList):
        self.Machines = [ [] for x in range(MachineNumber)]
        self.JobNotDone = []
        self.Jobs = JobList
    def find_machine(self, Job):
        # find a machine without schedule conflict, used ones prefered
        smallest_array = []
        # list record the how close of the input Job's starting time 
        # with the machine's end time
        # we want to choose the smallest gap, because that gives the 
        # largest space for other jobs
        how_many_does_not_fit = 0
        # If the job is not fit with the cunrrent selected machine
        # this number add 1
        
        for machine in self.Machines: # select a machine
            if not machine:     
            #  if machine == [], the end time of this machine is 0
            #  so, the gap is just the Job's starting time
                smallest_array.append(Job.startTime)
            else:
                if machine[-1].endTime <= Job.startTime:
                 # check if the current select job is not conflict
                 # with the last job in the selected machine
                 # then the gap between them is 
                 # Job starting time - endtime of machine
                    smallest_array.append(Job.startTime-machine[-1].endTime)
                else:
                # else, this job is conflict with the current machine
                    smallest_array.append(9999999999)
                    how_many_does_not_fit = how_many_does_not_fit + 1
        if  how_many_does_not_fit == len(self.Machines): 
            # if job conflict with all machine
            # can not schedule this job          
            self.JobNotDone.append(Job)
            return
        else:
            # find the machine with has the smallest gap with this job
            # add the job to that machine
            ind = smallest_array.index(min(smallest_array))
            self.Machines[ind].append(Job)
            return
    def make_schedule(self):
        # Sort each job in Jobs or say JobList
        # with the ealist end time at the first in the list and latest end time will
        # be the last item in the list
        sorted_job = sorted(self.Jobs, key = lambda x: x.endTime, reverse = False)
        # the sorted function is O(nlog(n)) in python
        for job in sorted_job:
            self.find_machine(job)

