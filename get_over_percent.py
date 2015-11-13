#!/usr/bin/python
# usage : python get_over_percent.py <input> <output>
# example : python get_over_percent.py Singlecell-blast-to-RefSeq-rna.out.txt Singlecell_over_97.txt

import sys
fread = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')
count = 0
counttotal = 0
for line in fread:
    tempcol = line.strip().split('\t')
    counttotal += 1
    if (float(tempcol[2])>97):
        fwrite.write(line.strip()+'\n')
        count += 1

print "You have "+str(count)+" over "+str(counttotal)+" sequences have above 97% Identity which is "+str(count*100/counttotal)+"% of total"
