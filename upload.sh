PI="pi@192.168.1.38"
ssh $PI "rm -rf /home/pi/software"
scp -r src "${PI}:/home/pi/software"
ssh $PI "python3 /home/pi/software/main.py"