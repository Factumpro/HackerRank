#!/bin/bash
read val
for((X=1;X<=val;X++))
do
    read num
    sum=$((sum + num))
done
echo "scale = 5; $sum/$val" | bc | xargs printf "%.3f\n"