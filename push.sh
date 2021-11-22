#!/bin/bash

set -x
set -e

echo $1


git add *.tjp *.tji *.sh


echo '?:' $?

if [ -z $1 ]; then git commit -m"<auto push>"; else git commit -m"$1"; fi

echo '?:' $?

git push

echo '?:' $?

git diff

