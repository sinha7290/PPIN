#!/bin/bash
File="13_14.txt"
Lines=$(cat $File)
for Line in $Lines
do 
	grep "$Line" hppin_sort2.txt | head -1 >> out.txt 

done
sort -nk 3 out.txt | head -n 1

