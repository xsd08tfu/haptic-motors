#!/bin/zsh
echo "Auto updating Haptic Band script"
sleep 5

ping -c 2 www.google.com
 
if [ $? != 0 ] 
then
   echo "does not have internet"
   python3 main.py
else
   echo "has internet"
   git pull && python3 main.py
fi