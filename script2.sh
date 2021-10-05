#!/bin/bash

printf "Content-type: text/html\n\n"
printf " "

printf "<center><h1>Welcome to my humble abode</h1></center>"

grep "GET[[:space:]]/cgi-bin/script2.sh[[:space:]]HTTP/1.1[[:space:]]200" -c access.log