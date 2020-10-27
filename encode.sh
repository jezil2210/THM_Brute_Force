#!/bin/bash

file="/home/jezil2210/$1"

echo $file

while IFS= read -r line
do 
  echo $line  | md5sum | cut -f1 -d '-' >> passwdEndoded.txt
done < $file




