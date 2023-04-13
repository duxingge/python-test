import os


ps = [3308, 6379,  5672, 27019, 2101]
ps = [ str(p) for p in  (ps + list(range(2001,2016)))]
for p in ps :
    # xargs is used to pass the output of the lsof command as arguments to the kill command.
    os.system(f"lsof -t -i tcp:{p} | xargs kill")

# kill -9 $(lsof -t -i tcp:2001-2016)