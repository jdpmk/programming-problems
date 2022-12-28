#!/bin/sh

set -xe

mkdir $1

echo "#include <iostream>

int main() {
    return 0;
}" > $1/main.cpp

echo "all:
	clang++ -std=c++17 -Wall -Wextra -pedantic main.cpp && ./a.out < example.in" > $1/Makefile
