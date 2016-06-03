#!/usr/bin/python
#usage: python cutoff.py refsoil_empsoil_blast_e5.out identity length
import sys
fread = open(sys.argv[1],'r')
#per = 97.0
per = float(sys.argv[2])

#le = 72
le = float(sys.argv[3])
now = ""
for line in fread:
    spl = line.strip().split('\t')
    if (float(spl[2]) < per):
        continue
    if (int(spl[3]) < le):
        continue
    if not (now == spl[0]):
        print line.strip()
        now = spl[0]
