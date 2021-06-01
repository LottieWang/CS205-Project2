#!/usr/bin/bash

file_name=" data/small/CS205_small_testdata__10 data/small/CS205_small_testdata__19 data/small/CS205_small_testdata__23 data/small/CS205_small_testdata__40 data/large/CS205_large_testdata__31 "
for file in $file_name
do
    echo "$file forward"
    python -u project2.py $file.txt 0 | tee $file.forward
done
