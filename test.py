import Schedule
import Job
import ReadInput
# This program includes read input file
# run the algorithm on the data
# output the result

# read from input file 
n_job,n_machine,  jobList = ReadInput.ReadInput("input.txt")

print("The list of Jobs is:\n", jobList)
print("There are %d machines\n" %n_machine)
# run the algorithm 
schedule = Schedule.Schedule(n_machine, jobList)
schedule.make_schedule()

# output the result
with open("Output.txt", "w") as text_file:
    print(n_job-len(schedule.JobNotDone), file=text_file)
    for i in range(n_machine):
    	print(end = '\n',file=text_file)
    	for j in range(len(schedule.Machines[i])):
    		print(schedule.Machines[i][j].jid, end = ' ',file=text_file)
    	print(end = '\n',file=text_file)




#print("The first machine has:\n", schedule.Machines[0])
#print("The second machine has:\n", schedule.Machines[1])
#print("The second machine has:\n", schedule.Machines[2])
#print("The unfinished jobs are:\n", schedule.JobNotDone)
#print(jobList)