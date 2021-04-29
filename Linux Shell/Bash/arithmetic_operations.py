#!/bin/bash
read num
echo "scale = 5; $num" | bc | xargs printf "%.3f\n"
