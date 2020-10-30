import time,sys,os,re
if len(sys.argv) != 3:
    sys.exit("Usage: python3 tailf file pattern")
else:
    infile = sys.argv[1]
    if not os.path.exists(infile):
        sys.exit("{} not existed".format(infile))
    pattern = sys.argv[2]

def follow(thefile):
    thefile.seek(0,2) # go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line.strip() # remove \n
def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line

logfile  = open(infile)
loglines = follow(logfile)
for line in grep(pattern, loglines):
    print(line) 
