#!/bin/bash

echo "3, 2, 1, GO!!!"
cd ../data
file=hash.txt

if [ ! -e "$file" ] ; then
    touch "$file"

else
    rm "$file"
    touch "$file"
fi

cat personal.txt | md5sum >> "$file"

cat  personal.txt | sha1sum >> "$file"

cat personal.txt | sha224sum >> "$file"

cat personal.txt | sha256sum >> "$file"

cat personal.txt | sha384sum >> "$file"

cat personal.txt | sha512sum >> "$file"

cat personal.txt | b2sum >> "$file"

echo "Finish :-)"