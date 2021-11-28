#!/bin/bash
g++ -std=c++11 -o $1 $1.cpp

if [ -z $3 ]
then
    ./$1
else
    ./$1 < $3
fi

if [ "$2" == 0 ]
then
    # continue without removing the file
    exit 0
else
    rm -f $1
fi
