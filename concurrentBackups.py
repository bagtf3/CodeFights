def concurrentBackups(threads, documents):
    import copy
    
    for d in documents:
        if d < 0:
            raise Exception
            
    if len(documents) == 0:
        return 0
    
    elif len(documents) <= threads:
        return max(documents)
    
    dcopy = documents[:]
    dcopy.sort()
    mx = dcopy.pop(len(dcopy)-1)
    
    tot = [[] for i in xrange(threads -1)]
    
    for i in xrange(len(tot)):
        tot[i].append(dcopy.pop(0))
    
    tot = tot + [[mx]]
    
    if dcopy:
        while dcopy:
            for i in xrange(len(tot)):
                try:
                    tot[i].append(dcopy.pop(0))
                except:
                    break
    
	#not sure much wiggle room you need, but at least as many as you have documents
	#should be fine
	
    for extra in xrange(len(documents):
        for i in xrange(len(tot)):
            tot[i].append(0)
    
    def findMin(tot, documents):
        
        tot_list = [sum(a) for a in tot]
        mx = tot_list.index(max(tot_list))
        temp = copy.deepcopy(tot)
        temp.sort(key = lambda x: sum(x))
        burn = [a.sort() for a in temp]
        mxitem = temp[-1]
        toSwitch = min([i for i in mxitem if i != 0])
        
        breakFlag = 0
        flag = 0
        for i in temp[:-1 or None]:
            if breakFlag == 1:
                break
            for j in i:
                if j < toSwitch:
                    temptemp = copy.deepcopy(temp)
                    mxitem = temptemp[-1]
                    mxitem[mxitem.index(toSwitch)] = j
                    temptemp[temptemp.index(i)][i.index(j)] = toSwitch
                    if max([sum(a) for a in temptemp]) < max(tot_list):
                        flag = 1
                        tot = temptemp
                        breakFlag = 1
                        break
        
        if flag == 0:
            return max([sum(a) for a in tot])
        
        else:
            return findMin(tot, documents)
    
    return findMin(tot, documents)
