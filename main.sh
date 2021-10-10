#!/bin/zsh
echo "Auto updating Haptic Band script"
echo "Sleeping fof 5 seconds to allow network connection"
sleep 5

ping -c 2 www.google.com
 
if [ $? != 0 ] 
then
   echo "does not have internet"
   python3 /home/pi/code/haptic-motors/main.py
else
   echo "has internet"
   cd /home/pi/code/haptic-motors/
   git pull && python3 main.py
fi