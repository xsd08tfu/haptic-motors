#!/bin/zsh
ping -c 2 www.google.com
 
if [ $? != 0 ] 
then
   echo "does not have internet"
else
   echo "has internet"
fi