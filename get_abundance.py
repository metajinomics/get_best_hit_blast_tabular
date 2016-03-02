#!/usr/bin/python
#usage: python get_abundance.py blast.out.txt summary.txt > output
import sys

blastread = open(sys.argv[1],'r')
sumread = opne(sys.argv[2],'r')

dict = {}
line = sumread.next()
while line != "Counts/sample detail:":
    line = sumread.next()
line = sumread.next()
for line in sumread:
    spl = line.strip().split(": ")
    dict[spl[0]]=spl[1]

for line in blastread:
    spl = line.strip().split('\t')
    if(dict.has_key(spl[1]):
           print spl[1]+'\t'+dict[spl[1]]
