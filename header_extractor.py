from tika import parser

#generalization to input pdf will be added
filein = parser.from_file('autoMLcode_GD.pdf')
textrawin=(filein['content']).strip().split('\n')
rawlinesarray=[]
for line in textrawin:
    rawlinesarray.append(line)

numofvar=(rawlinesarray[0].replace('Number of variables: ',''))
rawinvarnames=(rawlinesarray[1].replace('Input: ','').split(','))
#period should be removed from end of input
invardims=[] #if the value is zero, the entry is a scalar
invarnames=[]
for entry in rawinvarnames:
    newentry=entry.strip()
    if 'R' in newentry:
        splitind=newentry.find('R')
        rawdim=(newentry[splitind+1:len(newentry)])
        invardims.append(rawdim.split('×'))
        invarnames.append(newentry[0:splitind].strip())
    else:
        invardims.append(0)
        invarnames.append(newentry.strip())
rawoutvarnames=(rawlinesarray[2].replace('Output: ','').split(','))
outvardims=[]
outvarnames=[]
for entry in rawoutvarnames:
    newentry=entry.strip()
    if 'R' in newentry:
        splitind=newentry.find('R')
        rawdim=(newentry[splitind+1:len(newentry)])
        outvardims.append(rawdim.split('×'))
        outvarnames.append(newentry[0:splitind].strip())
    else:
        outvardims.append(0)
        outvarnames.append(newentry.strip())
#above section extracts both the input and output variable information
#from a pseudcode header
for x in range(0,len(invardims)):
    print(invarnames[x])
    print(' ')
    print(invardims[x])
    print("\n")
