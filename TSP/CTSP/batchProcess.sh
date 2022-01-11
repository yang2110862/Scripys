#!/bin/bash
# Program:
#       Run data for revised ITPLS in instances setII
# History:
# 2021/12/26    yxl     First version
InstancesRoute='/home/seanyang/Desktop/git/CTSP/Instances/set II'
ExeFile='/home/seanyang/Desktop/git/CTSP/codes/ITPLS/ils_ctsp'
TimeLen=600
for file in `ls "$InstancesRoute"`
do
        if [ "$file" == 'README.txt' ] ; then
                continue
        fi
        num=${file%%_*[a-z]}
        num=${num##[a-z]*[a-z]}
        declare -i num_v=$num-1
        for seed in $(seq 1 10)
        do
                echo "$file $num_v $TimeLen $seed"
                "$ExeFile" "$InstancesRoute"/"$file" "$num_v" "$TimeLen" "$seed"
        done
done
