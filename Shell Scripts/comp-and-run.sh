#!/bin/bash

#Simple and stupid script that compiles(tries to altleast) an entire folder
#and generates a single binary output and then tries to run it

echo
proj_folder=$(ls . | fzf)
proj_files=$(find $proj_folder | sed '1d; /\.ccls-cache/d')

gcc $proj_files -o $proj_folder-test -lm -Wall -Wextra
./$proj_folder-test

echo 
echo
