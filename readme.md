# Raspberry Pi Relay Controller for the ModMyPi Relay board

The [ModMyPi PiOT Relay Board](https://www.modmypi.com/raspberry-pi/breakout-boards/modmypi/modmypi-piot-relay-board) is a 4-port relay controller board for the Raspberry Pi. 
   
## Hardware Components

To use this project, you'll need at a minimum the following hardware components:

+ [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
+ [ModMyPi PiOT Relay Board](https://www.modmypi.com/raspberry-pi/breakout-boards/modmypi/modmypi-piot-relay-board)
+ 5V, 2.5A Micro USB power source (basically, a smartphone charger) - I use the [CanaKit 5V 2.5A Raspberry Pi 3 Power Supply/Adapter/Charger](https://www.amazon.com/gp/product/B00MARDJZ4)
 
## Assembly

To assemble the hardware, mount the relay board on the Raspberry Pi as shown in the following figure. The relay board is designed for older Raspberry Pi's (they have less GPIO pins), so, as you can see, not all of the pins from the relay board will connect to the Raspberry Pi.  

## Configuring Your Raspberry Pi

Download the latest version of the Raspbian OS from the [Raspberry Pi web site](https://www.raspberrypi.org/downloads/raspbian/) and follow the [instructions](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) for writing the OS image to a Micro SD card for the Pi. Insert the **SD card** in the Pi, connect **Ethernet**, **keyboard**, **mouse**, and a **monitor** to the Pi and finally **power it up** using a smartphone charger or some suitable power source.

Raspbian comes configured with its keyboard, timezone, and other locale settings configured for the United Kingdom (UK), so if you're in the US, or elsewhere that's not the UK, you'll want to switch over to the **localisation** tab and adjust the settings there as well.

When the Pi comes back up, open a terminal window and execute the following command:

	sudo apt-get update

This updates the local catalog of applications. Next, execute the following command:

	sudo apt-get upgrade

This command will update the Raspbian OS with all updates released after the latest image was published. The update process will take a long time, so pay attention, answer any prompts, and expect this process to take a few minutes or more (the last time I did this, it took about 15 minutes or more to complete).

Install library...


## Software Installation

The controller's Flask application uses Flask and the Flask Bootstrap plugin to serve [Bootstrap](http://getbootstrap.com/) applications, so in the terminal window, install the plugin by executing the following command:  

	sudo pip install flask flask_bootstrap

Finally, clone the controller application to your local system. Assuming your terminal window is currently pointing to the `Seed-Studio-Relay-Board` folder, navigate back to the `pi` user's home folder and clone the repository by executing the following commands:

	cd .. 
	git clone REPO
	cd REPO

Your terminal window should look something like this:
 

## Update History

Nothing yet.

***
By [John M. Wargo](http://www.johnwargo.com) - If you find this code useful, and feel like thanking me for providing it, please consider making a purchase from [my Amazon Wish List](https://amzn.com/w/1WI6AAUKPT5P9). You can find information on many different topics on my [personal blog](http://www.johnwargo.com). Learn about all of my publications at [John Wargo Books](http://www.johnwargobooks.com). 