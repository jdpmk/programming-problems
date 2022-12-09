#!/bin/sh

set -xe

cat input/1.data | paste -sd '+' - | sed 's/++/\
    /g' | bc | sort -nr | head -n 1
