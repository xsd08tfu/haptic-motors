#!/bin/sh

ping -c2 google.com 

 
if [ $? != 0 ] 
then
   echo "has internet"
else
   echo "does not have internet"
fi