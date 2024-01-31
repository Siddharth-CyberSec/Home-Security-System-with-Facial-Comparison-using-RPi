OBJECTIVE<br>
Home Security Systems are a need of the modern-day houses. It is possible to design a simple home security solution by using Raspberry Pi and utilizing the power of Internet of Things. The home security system designed in this project is a simple and easily installable device built using Raspberry Pi 3, Web Cam and PIR Motion Sensor. The Raspberry Pi 3 Model B comes equipped with on-board Bluetooth (BLE) and Wi-Fi (BCM43438 Wireless LAN), so, it can be easily connected with a Wi-Fi Router to access a cloud service. 


The device designed in this project can be installed at the main entrance of a house. It detects motion of any visitor with the help of PIR sensor and starts capturing the images with the help of a USB web cam. The images are temporarily stored on the Raspberry Pi and pushed to the Google Cloud from where they are sent as email alert to the house owner. So, the user gets the images of any visitor immediately on email which he can check from his smart phone. The Raspberry Pi connects with the Google Cloud over TCP-IP stack. The Raspberry Pi 3 is one of the IoT boards which comes equipped with on-board TCP/IP stack, so, it can be readily connected to an IoT network. The Pi uses OpenCV library to capture images from the Web Cam and send them over registered Email address of the user.


The home security system designed in this project, though being simple, is a powerful application. The user can keep surveillance of his house from anywhere, any time and always by just installing this small device at the main entrance. Many such devices can also be installed to further add security layers. The entrance of any intruder can be detected and alerted by the Email on the smart phone, then the user is free to take appropriate action like calling police, informing law enforcement etc.    



COMPONENTS REQUIRED<br>
Components	Quantity<br>
Raspberry Pi (4B Model) (4GB)	1<br>
PIR Sensor	1<br>
Raspberry Pi Noir Camera v2.1 (5MP)	1<br>
Power Adapter 5V/1.5A	1<br>
Female-to-Female (Jumper Wires)	3<br>
Micro HDMI to HDMI Cable	1<br>
Micro SD card (32 GB)	1<br>
SD Card Reader	1<br>
Raspberry Pi Case	1<br>



PIR Sensor:<br>
The PIR (Passive Infra-Red) Sensor is a Pyroelectric device that detects motion by measuring changes in the infrared levels emitted by surrounding objects. By incorporating a Fresnel lens and motion detection circuit, the module provides high sensitivity and low noise. The module provides an optimized circuit that can detect motion up to 6 meters away. There are two slots on the sensor, each made up of a special IR sensitive material. In the absence of anybody, the two slots receive the same amount of IR radiation. When a person passes by the sensor, it is intercepted by one half of the slots causing a positive potential difference across the slots. When the person leaves by the sensor, it is intercepted by another half of the slots causing a negative potential difference across the slots. This positive and negative differential generates a pulse thus detecting motion.
The sensor module has on-board 3.3 V voltage regulator, protection diode, sensitivity adjustment and delay time adjust. There are three terminals on the module – ground, VCC and Digital Out. A voltage of 5V to 12 V can be supplied at the VCC pin, though 5V is the recommended power supply. When the module detects motion, the output at the Digital Out pin goes HIGH. This is a standard 5V active high signal.  The Digital Out pin of the sensor is connected to GPIO pins of Raspberry Pi directly to monitor signal. It is connected to GPIO 4th pin of Raspberry pi 3. The VCC pin of the module is connected to one of the 5V DC Power pin of the Pi 3 and ground pin of the module is connected to one of the ground pins of the Pi. 



Camera:<br>
On 14 May 2013, the foundation and the distributors RS Components & Premier Farnell/Element 14 launched the Raspberry Pi camera board alongside a firmware update to accommodate it. The camera board is shipped with a flexible flat cable that plugs into the CSI connector which is located between the Ethernet and HDMI ports. In Raspbian, the user must enable the use of the camera board by running Raspi-config and selecting the camera option. The camera module costs €20 in Europe (9 September 2013). It uses the OmniVision OV5647 image sensor and can produce 1080p, 720p and 640x480p video. The dimensions are 25 mm × 20 mm × 9 mm. In May 2016, v2 of the camera came out, and is an 8-megapixel camera using a Sony IMX219. 
Infrared Camera – In October 2013, the foundation announced that they would begin producing a camera module without an infrared filter, called the Pi NoIR. 



PROPOSED METHODOLOGY<br>
The IoT device built on Raspberry Pi 4B in this project has a simple and straight forward operation. The device detects motion by the PIR sensor and as it detects motion, it starts capturing video. The videos are stored on the MicroSD card and sent on the registered email of the user. All of this is managed by a python script running over the Raspberry Pi Operating System. Before running the python script, it is essential to install operating system on the Pi 4B and install the required libraries i.e. python3, numpy on the operating system. While installing the operating system, installing the libraries and the python script, the Raspberry Pi should be connected to a display monitor using HDMI cable or to your laptop/PC screen via internet

For installing the Raspbian Operating System on MicroSD card, first download the latest image of Raspbian OS from Raspberry Pi website. 

Flash the image of the latest Raspberry Pi OS in the MicroSD card. If the MicroSD card used is 32 GB or below, it must be formatted to FAT32 (file system) before copying the image or if the MicroSD card is more than 32 GB, it should be formatted to exFAT before copying the image. Flash the OS image using a flasher of your choice it to the Micro SD card. After flashing the extracted image, insert the card in the MicroSD slot as shown below – 
![image](https://github.com/Siddharth-CyberSec/Home-Security-System-with-Facial-Comparison-using-RPi/assets/86714257/062c1f23-0b61-4590-a823-28676f0085f3)
 

Getting started with Raspberry Pi without using HDMI Cable
After flashing the Raspberry Pi OS image on the SD card insert it into the Raspberry Pi, switch the power On and let it boot. After a few minutes switch off RPi and put it back on the laptop, now open the sd card and there should be boot folder with all the necessary files to start a RPi. Now open Notepad++, download and install it if you don’t have it, now write the following code in it:


>country=IE
>ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
>update_config=1
>network={
>scan_ssid=1
>ssid="your internet network name"

>psk=" your internet network password"
>key_mgmt=WPA-PSK

>}
>

Now save this file with the name “wpa_supplicant.conf” and save it as a CONF file.

Now create a EMPTY FILE with the name of “SSH” and copy both these files and paste it in the boot folder of the RPi SD Card.

Now Put the SD Card back in the Raspberry Pi and Switch it ON, let it run for a few minutes, during that time download and install a software called, “Nmap-Zenmap GUI”.

Now when you have installed the above software and the Raspberry Pi has been operational for a while now, first make sure that your laptop and the raspberry pi are both on the same network, open the Command Prompt in your laptop and type:

>nmap  -sn

this will give you a list of all the devices that are connected to your device, note the IP address of your raspberry pi device for further use. 

Now download install “Putty” and “VNC Viewer”, First open Putty and put in the IP address of your Raspberry Pi and click OPEN, this will open the terminal of your raspberry Pi device (*NOTE-Terminal is not the Raspberry Pi Graphical Interface/Screen, it is like the Command Prompt of your Raspberry PI). Login in the terminal as (if this is your first time then most probably) username-p, password-raspberry. And write the following command

>Sudo raspi config

And follow the below steps:
  1. Select Interfacing Options (number 5 on the list)
     ![image](https://github.com/Siddharth-CyberSec/Home-Security-System-with-Facial-Comparison-using-RPi/assets/86714257/7fd90f98-add1-434b-a347-0d836b51ba38)

  2. Select VNC (number 3 on the menu)
     ![image](https://github.com/Siddharth-CyberSec/Home-Security-System-with-Facial-Comparison-using-RPi/assets/86714257/848d778b-b972-47cc-993b-ccc84b45fb9e)

  3. Select Yes. 
     ![image](https://github.com/Siddharth-CyberSec/Home-Security-System-with-Facial-Comparison-using-RPi/assets/86714257/73573445-cbae-4b73-86b4-0219b628ed19)

  4. Hit Enter to acknowledge the VNC server is enabled.
     ![image](https://github.com/Siddharth-CyberSec/Home-Security-System-with-Facial-Comparison-using-RPi/assets/86714257/7d1fcadb-17a2-4b97-9c56-fb5034efb25a)

  5. Select Finish
     ![image](https://github.com/Siddharth-CyberSec/Home-Security-System-with-Facial-Comparison-using-RPi/assets/86714257/90fa7657-07bb-4648-a8da-efa3a9dd755f)

Now open VNC Viewer and put in the IP address of your Raspberry Pi device.  Now the Graphical User Interface between your Raspberry Pi and you will be visible, do the necessary settings and then open the terminal of your raspberry pi (a black box like the command prompt box on the top column), write the following commands.

>sudo apt-get update
>sudo apt-get upgrade

Now we have to install the libraries that we are going to use in our project.\

>sudo apt-get install python3-picamera

>sudo apt-get install gpac

>sudo apt-get install rpi.gpio

>pwd
>
>mkdir python_code
>
>cd python_code/
>
>mkdir capture

Copy the source code (given in the next Section) file and paste it in the Software_Engineering_Project/SidProject.py
(I named my python code file ‘surveillance.py’ for further reference)

Go back to the Terminal of Raspberry Pi and enter the Following Command

>cd Software_Engineering_Project/SidProject.py<br>
>ls<br>
>python3 SidProject.py<br>

That’s it, now if there is any movement in-front of the PIR Sensor it will detect it and the camera will record a video of 10 seconds and send it to your mail....


