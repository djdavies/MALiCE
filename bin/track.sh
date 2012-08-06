#!/bin/bash

### Track and save changes made to source files ###

# You need to create a directory called 'changes'
# in the same directory as your code.

version=$(date +%y%m%d-%H%M%S)
touch ./changes/$1.previous
touch ./changes/$1.current

mv ./changes/$1.previous ./changes/$1.$version
mv ./changes/$1.current ./changes/$1.previous
cp $1 ./changes/$1.current
