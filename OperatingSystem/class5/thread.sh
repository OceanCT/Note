#!/bin/bash
for ((i = 1; $i <= 1000; i++));
do
    echo $i
    ./thread 1
done