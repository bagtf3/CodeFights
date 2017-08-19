
#files= [[461618501,3], 
# [461618502,1], 
# [461618504,2], 
# [461618506,5], 
# [461618507,6]]
#backups= [461618501, 461618502, 461618504, 461618505, 461618506]


##### Not sure if this is working 
##### or not. Did not get to test it. 

def troubleFiles(files, backups):
    fileTimes = [f[0] for f in files]
    index_mask = []
    trouble = []
    
    for b in backups:
        theFiles = []
        if b == backups[0]:
            for f in xrange(len(fileTimes)):
                if fileTimes[f] <= b:
                    if f not in index_mask:
                        theFiles.append(f)
                        index_mask.append(f)
            
            runtime = sum([files[i][1] for i in theFiles])
            tr = -1
            if theFiles:
                for f in fileTimes:
                    #print f
                    if f <= b + runtime and f >= b:
                        #print "y"
                        tr += 1
                        index_mask.append(fileTimes.index(f))
            
            trouble.append(max([0,tr]))
            lastBackup = b
        
        elif b != backups[len(backups)-1]:
            for f in xrange(len(fileTimes)):
                if fileTimes[f] <= b and f not in index_mask:
                    theFiles.append(f)
                    index_mask.append(f)
                        
            runtime = sum([files[i][1] for i in theFiles])
            tr = -1
            if theFiles:
                for f in xrange(len(fileTimes)):
                    if fileTimes[f] < b + runtime and f not in index_mask:
                        tr += 1
                        index_mask.append(f)
            
            trouble.append(max([0,tr]))
            lastBackup = b
                
        else:
            for f in xrange(len(fileTimes)):
                if fileTimes[f] <= b and f not in index_mask:
                    theFiles.append(f)
                    index_mask.append(f)
                        
            runtime = sum([files[i][1] for i in theFiles])
            tr = -1
            if theFiles:
                for f in xrange(len(fileTimes)):
                    if fileTimes[f] < b + runtime and f not in index_mask:
                        tr += 1
                        index_mask.append(f)
            
            trouble.append(max([0,tr]))
            return trouble
            
                 
            
                
        
        
        
        
        
        
        