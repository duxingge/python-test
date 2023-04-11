import os


ps = [3308, 6379,  5672, 27019, 2101]
ps = ps + (list(range(2001,2016)))

for p in ps :
    os.system("for p in $( lsof -i tcp:"+str(p)+" | sed -n '1!p' |awk -F ' ' '{print $2}' | uniq ) ; do kill -9 $p ; done")

