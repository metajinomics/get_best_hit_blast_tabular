# Get_best_hit_blast_tabular

## To get the best hit from blast in tabular form
This script give you the file that contain the best hit of the BLAST in tabular form

You need GCC to compile.

```
g++ DownstreamBlast.cpp -o DownstreamBlast
./DownstreamBlast outtabular.txt result.txt
```

## To get only over 97% identity
```
python get_over_percent.py Singlecell-blast-to-RefSeq-rna.out.txt Singlecell_over_97.txt
```
## To get abundance information
```
python ../get_best_hit_blast_tabular/get_abundance.py sc_emp_blast.out.txt /mnt/data2/jin_emp/emp/soil_emp_table.summary > sc_emp_count.txt
```