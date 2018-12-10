class Job(object):
	#Create Job object that has attributes:
	#jib = job ID
	#startTime = Job stating time
	#endTime = Job's deadline

    def __init__(self, ID,  start, end):
        self.jid = int(ID)
        self.startTime = int(start)
        self.endTime = int(end)
        self.conpatibleCount = 0;
    def __repr__ (self):
    	# string reprsentation of jobs.
        return '%s: [%s, %s]\n' % (self.jid, self.startTime, self.endTime)
    
        #self.conpatibleCount = count;