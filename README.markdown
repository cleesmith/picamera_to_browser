# Sep 2014: Raspberry Pi
> Use picamera to capture a jpeg image then stream it to a web browser. 

> The jpeg image is never saved to disk, so it all happens in memory.

> Uses:
* just to take a photo remotely
* who's that knocking at my door

***

# Installation

## (1) on a Raspberry Pi

### ensure Python is installed:
```
python --version
```
> Only tested with python version 2.7.3

### ensure PIP is installed:
```
pip --version ... if not do:
sudo apt-get install python-dev
sudo apt-get install python-setuptools
sudo apt-get install python-pip
```

### install Picamera:
```
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
sudo apt-get install python-picamera
```

### install/start the Flask web app:
```
sudo pip install Flask
git clone https://github.com/cleesmith/picamera_to_browser.git
cd /picamera_to_browser
python capture_with_streamed_response.py
```

### use a web browser to capture and view a photo:
http://use_the_rpi_IP:5000/smile

### after testing, the red LED on the camera can be turned off:
```
sudo nano /boot/config.txt
... add this line:
disable_camera_led=1
sudo reboot
```
> Otherwise, the red LED causes a reflection if behind a pane of glass/plastic.

***
