creationTimes= [461620201, 461620203, 461620207]
backupRequests= [[1,0,461620202], 
 [1,2,461620208], 
 [0,2,461620210], 
 [1,0,461620204], 
 [1,1,461620209], 
 [1,1,461620203]]
k= 3
t= 461620210

def backupHistory(creationTimes, backupRequests, k, t):
    out = [0 for i in creationTimes]
    files = [fi for fi in creationTimes]
    for f in xrange(len(files)):
        time = files[f]
        backups = []
        while time + k <= t:
            time += k
            backups.append(time)
        
        relevant = [b for b in backupRequests if b[1] == f and b[2] <= t]
        relevant.sort(key = lambda x: x[2])
        
        for r in relevant:
            if r[0] == 0:
                new = [bac for bac in backups if bac < r[2]]
                backups = new[:]
        
        for r in relevant:
            if r[0] == 1:
                if r[2] not in backups:
                    backups.append(r[2])
        
        out[f] = len(backups)
    print out
                
        
        