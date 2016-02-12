#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
charRanks = allowedSpecialChars + "0123456789" + "aA-zZ" # {valid chars wth rank, usr dfnd / pltfrm dpndnt} what about k'a? get internationally accepted order
positionDict = dict(zip(charRanks, [None for _ in charRanks]))

def readAline(fh, initPos):
    bs = b""
    pickle.seek(initPos, BEG)
    while True:
        x = fh.read(1)
        if x is '\n':    break
        else:
            bs+= x
    return bs.encode()

def howDeep(test, std):
    for i, char in enumerate(std):
        if test[i] is char:    continue
        else: return i

def getExactPosition(name, fh): # why pickle, WHY NOT a real db?
    pos = 0 if positionDict[name[0]] is None else positionDict[name[0]]
    count = 0
    while True:
        l = readAline(fh)
        n = l.split('\t')[0]
        if n[0] not name[0]:
            return pos
        else:
            depth = howDeep(n, name)
            if depth is len(name): # check for (last) exact match of name in names(i.e. col1) if found insert after last match
            elif depth < len(name):
                pos+= len(l) + 1
                continue 
    return exactPos

def pickleDump():
    global positionDict
    finalStr = '\t'.join(data)
    ptrSeekValue = getExactPosition(data[0], pickleFileObj)
    pickle.seek(ptrSeekValue, BEG)
    pickle.dump(finalStr, pickleFileObj, protocol=-1)
    positionDict[data[0][0]] = ptrSeekValue + len(finalStr) #+= len(fs) coz None+int is bad
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
