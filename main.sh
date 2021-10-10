#!/bin/sh
ping -c 2 www.google.com
echo $?
 
if [ $? != 0 ] 
then
   echo "has internet"
else
   echo "does not have internet"
fi