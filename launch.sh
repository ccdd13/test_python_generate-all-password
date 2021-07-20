#!/usr/bin/env bash

s=""
for i in {a..z} ; do
  s="$s$i "
done
for i in {A..Z} ; do
  s="$s$i "
done
for i in {0..9} ; do
  s="$s$i "
done
chmod u+x *.sh *.py
echo generating all possible passwords from character set
echo -e "\n'$s'"
echo to ./generated/possible-passwords.txt
echo running ...
./main.py $s > ./generated/possible-passwords.txt
echo done.
ls -Flah --color=auto --group-directories-first
