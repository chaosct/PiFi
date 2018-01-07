# Installing Base System

First of all, you need a Raspberry Pi Zweo W. This is the one with WiFi.

We are just using Raspbian Lite.

1. Download the image from the [official website](https://www.raspberrypi.org/downloads/raspbian/)
2. Follow [instructions](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) to write the image to the SD card
3. Follow the [adafruit isntructions](https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget/ethernet-gadget) to enable USB network connection to the Raspberry Pi
4. Create an empty file with the name `SSH` to the SD root to enable ssh server at first boot
5. Boot your Rpi connected to the computer (you may need to install drivers)
6. Ssh to raspberrypi.local
7. Change password `$ passwd`
8. Run raspbian configuration tool to resize your partition and reboot
9. [Configure initial WiFi connection](https://thepihut.com/blogs/raspberry-pi-tutorials/83502916-how-to-setup-wifi-on-raspbian-jessie-lite) ([more details](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md))
10. update and upgrade
