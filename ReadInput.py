import Job

def ReadInput(filename):
    # read in the input file
    fp = open("input.txt", 'r')
    line = fp.readline().split()

    job_number = int(line[0])
    machine_number = int(line[1])
    jid = 0
    jobList = []
    # read all jobs and add to jobList
    while True:
        line = fp.readline()
        jid = jid + 1
        if not line:
            break
        time = line.split()
        start = time[0]
        end = time[1]
        job = Job.Job(jid, start, end)
        # add job
        jobList.append(job)
    fp.close()
    return job_number, machine_number, jobList
