
de>
brandon@farb:~$ sudo apt-get install libusb-1.0-0-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  libusb-1.0-0
The following NEW packages will be installed:
  libusb-1.0-0 libusb-1.0-0-dev
0 upgraded, 2 newly installed, 0 to remove and 8 not upgraded.
Need to get 172kB of archives.
After this operation, 1073kB of additional disk space will be used.
Do you want to continue [Y/n]? y
Get:1 http://us.archive.ubuntu.com jaunty/universe libusb-1.0-0 2:1.0.0-1 [29.8kB]
Get:2 http://us.archive.ubuntu.com jaunty/universe libusb-1.0-0-dev 2:1.0.0-1 [142kB]
Fetched 172kB in 0s (207kB/s)       
Selecting previously deselected package libusb-1.0-0.
(Reading database ... 200342 files and directories currently installed.)
Unpacking libusb-1.0-0 (from .../libusb-1.0-0_2%3a1.0.0-1_i386.deb) ...
Selecting previously deselected package libusb-1.0-0-dev.
Unpacking libusb-1.0-0-dev (from .../libusb-1.0-0-dev_2%3a1.0.0-1_i386.deb) ...
Processing triggers for doc-base ...
Processing 1 added doc-base file(s)...
Registering documents with scrollkeeper...
Setting up libusb-1.0-0 (2:1.0.0-1) ...

Setting up libusb-1.0-0-dev (2:1.0.0-1) ...

Processing triggers for libc6 ...
ldconfig deferred processing now taking place
</code>

<code>
tar xzvf labjack-exodriver-f4c2cdd.tar.gz
cd labjack-exodriver-f4c2cdd/liblabjackusb/
</code>

<code>
brandon@farb:~/Desktop/labjack-exodriver-f4c2cdd/liblabjackusb$ make -f Makefile.Linux 
cc -fPIC -g -Wall -c labjackusb.c
cc -shared -Wl,-soname,liblabjackusb.so -o liblabjackusb.so.2.0.1 labjackusb.o -lusb-1.0 -lc 
</code>

<code>
brandon@farb:~/Desktop/labjack-exodriver-f4c2cdd/liblabjackusb$ sudo make install
install liblabjackusb.so.2.0.1 /usr/local/lib
ldconfig /usr/local/lib
</code>

<code>
brandon@farb:~/Desktop/labjack-LabJackPython-9b9f008/src$ sudo python setup.py install
[sudo] password for brandon: 
running install
running build
running build_py
running install_lib
copying build/lib.linux-i686-2.6/u12.py -> /usr/local/lib/python2.6/dist-packages
copying build/lib.linux-i686-2.6/u6.py -> /usr/local/lib/python2.6/dist-packages
copying build/lib.linux-i686-2.6/u3.py -> /usr/local/lib/python2.6/dist-packages
copying build/lib.linux-i686-2.6/LabJackPython.py -> /usr/local/lib/python2.6/dist-packages
copying build/lib.linux-i686-2.6/ue9.py -> /usr/local/lib/python2.6/dist-packages
copying build/lib.linux-i686-2.6/Modbus.py -> /usr/local/lib/python2.6/dist-packages
byte-compiling /usr/local/lib/python2.6/dist-packages/u12.py to u12.pyc
byte-compiling /usr/local/lib/python2.6/dist-packages/u6.py to u6.pyc
byte-compiling /usr/local/lib/python2.6/dist-packages/u3.py to u3.pyc
byte-compiling /usr/local/lib/python2.6/dist-packages/LabJackPython.py to LabJackPython.pyc
byte-compiling /usr/local/lib/python2.6/dist-packages/ue9.py to ue9.pyc
byte-compiling /usr/local/lib/python2.6/dist-packages/Modbus.py to Modbus.pyc
running install_egg_info
Writing /usr/local/lib/python2.6/dist-packages/LabJackPython-0.7.egg-info
</code>

<code>
dmesg
. . .
[3974830.576068] usb 4-1: new full speed USB device using uhci_hcd and address 7
[3974830.739804] usb 4-1: configuration #1 chosen from 1 choice
</code>

<code>
brandon@farb:~/Desktop/labjack-exodriver-f4c2cdd/liblabjackusb$ sudo python
Python 2.6.2 (release26-maint, Apr 19 2009, 01:56:41) 
[GCC 4.3.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import u3
>>> d = u3.U3()
>>> d.open()
>>> d.configU3()
{'TimerClockConfig': 2, 'TimerClockDivisor': 256, 'LocalID': 1, 'SerialNumber': 320035020, 'CIOState': 0, 'TimerCounterMask': 64, 'DAC1Enable': 0, 'EIODirection': 0, 'DeviceName': 'U3-LV', 'FIODirection': 0, 'FirmwareVersion': '1.12', 'CIODirection': 0, 'DAC0': 0, 'DAC1': 0, 'EIOAnalog': 0, 'CompatibilityOptions': 0, 'EIOState': 0, 'HardwareVersion': '1.30', 'FIOAnalog': 0, 'VersionInfo': 2, 'FIOState': 0, 'BootloaderVersion': '0.27', 'ProductID': 3}
</code>

<code>
cd ..
sudo cp 10-labjack.rules /etc/udev/rules.d
sudo udevadm control --reload-rules
</code>
