import time,sys,os,re
if len(sys.argv) != 2:
    sys.exit("Usage: python3 tailf file")
else:
    infile = sys.argv[1]
    if not os.path.exists(infile):
        sys.exit("{} not existed".format(infile))

def follow(thefile):
    thefile.seek(0,2) # go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line.strip() # remove \n

logfile = open(infile)
for line in follow(logfile):
    print(line) 
