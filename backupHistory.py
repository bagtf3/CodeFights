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
    return out
                
        
        
