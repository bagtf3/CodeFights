#files= ["F1", 
 #"F2", 
 #"F3", 
 #"F4", 
 #"F5", 
 #"F6", 
 #"F7", 
 #"F8", 
 #"F9"]
#parents= ["-1", 
 #"F1", 
 #"F1", 
 #"F3", 
 #"F3", 
 #"F3", 
 #"F6", 
 #"F6", 
 #"F2"]
#file1= "F7"
#file2= "F3"

#closestCommonParent(files, parents, file1, file2) = "F2".
def closestCommonParent(files, parents, file1, file2):
    
    def isParent(par, chi, mapping):
        return par == next(p[0] for p in mapping if p[1] == chi)
    
    def getFamily(file1, parents, mapping, stopLen):
        breakFlag = 0
        stopCount = 0
        flist = [file1]
        look1 = file1
        
        while breakFlag == 0:
            for p in list(set(parents)):
                if isParent(p, look1, mapping):
                    flist.append(p)
                    look1 = p
                    break
                else:
                    stopCount += 1
            if stopCount == stopLen or look1 == "-1":
                breakFlag = 1
        return flist
        
        
    stopLen = len(list(set(parents)))
    mapping = [[x,y] for x,y in zip(parents, files)]
    
    f1_list = getFamily(file1, parents, mapping, stopLen)
    f2_list = getFamily(file2, parents, mapping, stopLen)
    
    firstMatch = ""
    breakFlag = 0
    
    for i in f1_list:
        if breakFlag == 1:
            break
        for j in f2_list:
            if i == j:
                firstMatch = i
                breakFlag = 1
                break
    
    return firstMatch
    
    
        
        
        