def cpuEmulator(subroutine):
    
    regs = ["R" + str(r).zfill(2) for r in xrange(0, 43)]
    registers = {r: 0 for r in regs}
    
    i = 0
    while i < len(subroutine):
        
        #print subroutine[i]
        try:
            del(a);del(b0);del(b1)
        except:
            burn = ""
        
        if subroutine[i] == "NOP":
            i += 1
            continue
        
        a,b0 = subroutine[i].split()
        
        if len(b0.split(',')) > 1:
            
            b0, b1 = b0.split(',')
        
        #### Program start here

        if a == "MOV":
            if b0[0] == "R":
                registers[b1] = int(registers[b0])
                i+=1
            else:
                registers[b1] = int(b0)
                i+=1
        
        elif a == "ADD":
            registers[b0] = int((registers[b0] + registers[b1]) % 2**32)
            i+=1
        
        elif a == "DEC":
            if registers[b0] > 0:
                registers[b0] -= 1
                i+=1
            else:
                registers[b0] = (2**32) -1
                i+=1
    
        elif a == 'INC':
            if registers[b0] < (2**32) -1:
                registers[b0] += 1
                i+=1
            else:
                registers[b0] = 0
                i+=1
        
        elif a == "INV":
            i+=1
            new = []
            for t in bin(registers[b0])[2:].zfill(32):
                if t == '0':
                    new.append('1')
                else:
                    new.append('0')
                    
            registers[b0] = int(''.join(new), 2)
            del(new)
        
        elif a == "JMP":
            i = int(b0) -1
        
        elif a == "JZ":
            if registers['R00'] == 0:
                i = int(b0) -1
            else:
                i += 1
    #print registers
    return registers['R42'] % 2**32
                