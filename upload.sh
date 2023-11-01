ssh pi@192.168.1.17 "rm -rf /home/pi/software"
scp -r src pi@192.168.1.17:/home/pi/software
ssh pi@192.168.1.17 "python3 /home/pi/software/main.py"