#!/bin/sh
i=0

while read params; do    
    python runner.py $params &
    ((i++))
done < params.txt
