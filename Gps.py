#camera 
i. sudo raspi-config
ii. sudo reboot
iii. libcamera-hello
iv. For image: libcamera-still -o image.jpg
v. For video: libcamera-vid -o video.h264 -t 10000


#GPS
#vcc 2 gnd 6 tx 10

Step 1 — Create a virtual environment

sudo apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate

Step 2 — Free up the serial port (enter one at a time)
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
sudo systemctl enable serial-getty@ttyAMA0.service

Step 3 — Install minicom
sudo apt-get install minicom
pip install pynmea2 --break-system-packages
sudo cat /dev/ttyS0
