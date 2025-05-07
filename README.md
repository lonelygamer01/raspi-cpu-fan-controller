# raspi-cpu-fan-controller
This little python script made for controlling the raspberry pi 5 fan connected on the pwm port.
The cooler is an Armor V5 black aluminium cooler, looks cool and gets to job done.

Reqirements:
- install python3
- place the script somewhere and edit the pwm path and/or the speed steps if desired
- make the daemon in the "sudo nano /etc/systemd/system/" folder
- reload deamon
sudo systemctl daemon-reload
sudo systemctl enable "name of deamon"
sudo systemctl start "name of deamon"

-DONE-
