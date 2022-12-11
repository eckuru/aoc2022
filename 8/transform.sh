#!/usr/bin/sh

sed -i 's/[0-9]/\0 /g' $1
