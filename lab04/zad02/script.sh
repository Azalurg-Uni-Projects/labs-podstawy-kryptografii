#!/bin/bash

echo "3, 2, 1, GO!!!"
cd ../data
file=diff-zad02.txt

if [ ! -e "$file" ] ; then
    touch "$file"
else
    rm "$file"
    touch "$file"
fi

cat hash-.pdf personal.txt | md5sum >> "$file"
cat hash-.pdf personal_.txt | md5sum >> "$file"

cat hash-.pdf personal.txt | sha1sum >> "$file"
cat hash-.pdf personal_.txt | sha1sum >> "$file"

cat hash-.pdf personal.txt | sha224sum >> "$file"
cat hash-.pdf personal_.txt | sha224sum >> "$file"

cat hash-.pdf personal.txt | sha256sum >> "$file"
cat hash-.pdf personal_.txt | sha256sum >> "$file"

cat hash-.pdf personal.txt | sha384sum >> "$file"
cat hash-.pdf personal_.txt | sha384sum >> "$file"

cat hash-.pdf personal.txt | sha512sum >> "$file"
cat hash-.pdf personal_.txt | sha512sum >> "$file"

cat hash-.pdf personal.txt | b2sum >> "$file"
cat hash-.pdf personal_.txt | b2sum >> "$file"

echo "Finish :-)"