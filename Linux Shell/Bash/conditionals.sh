#!/bin/bash
read val
if [[ $val == [Yy] ]]
then
    echo 'YES'
elif [[ $val == [Nn] ]]
then
    echo 'NO'
fi