#!/usr/bin/python
#usage: python get_abundance.py blast.out.txt summary.txt > output
import sys

blastread = open(sys.argv[1],'r')
sumread = open(sys.argv[2],'r')

dict = {}
line = sumread.readlines()
while line != "Counts/sample detail:":
    line = sumread.readlines()
line = sumread.readlines()
for line in sumread:
    print line
    spl = line.strip().split(": ")
    dict[spl[0]]=spl[1]

for line in blastread:
    spl = line.strip().split('\t')
    if(dict.has_key(spl[1])):
           print spl[1]+'\t'+dict[spl[1]]
