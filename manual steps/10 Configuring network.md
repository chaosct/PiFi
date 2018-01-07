# Configuring Network

enabling wifi again

http://weworkweplay.com/play/automatically-connect-a-raspberry-pi-to-a-wifi-network/
https://www.raspberrypi.org/forums/viewtopic.php?t=191061#p1199674

`$ sudo systemctl enable wpa_supplicant.service`

## final `/etc/network/interfaces`:

```
# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto usb0
allow-hotplug usb0
iface usb0 inet static
	address 10.254.239.1
	netmask 255.255.255.0
	network 10.254.239.0
	broadcast 10.254.239.255

allow-hotplug wlan0
iface wlan0 inet dhcp
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    interface default inet dhcp
```

https://raspberrypi.stackexchange.com/questions/48307/sharing-the-pis-wifi-connection-through-the-ethernet-port
