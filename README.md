# IDS
Intrusion Detection System Raspberry Pi

Synopsis
The system was developed for HackerEarth Internet of Things (IOT) Hackathon in 24 hours.
The system detects motion using an ultrasound sensor, which triggers a camera, then the the images and video of intruder are transmitted to the user via mail and instant messaging app, Telegram.
It was developed in a team of two: Arpit Jain and Saksham Gupta.

Video Link: https://youtu.be/TxEb-Dn5gjg
Presentation: https://he-s3.s3.amazonaws.com/media/sprint/internet-of-things-india-hacks-2016/team/37793/f696bfbHACHEREARTH_IOT.pptx

Objective: Our system alerts the user in real time along with the vital information about the culprit or intruder in their house; making the user capable of taking required action. The system further aims to protect homes from house fires.
Current Systems: Senses motion using a ultrasonic sensor, alerts the user through email and instant messaging (whatsapp, telegram) along with images and videos of the intruder. The current system uses a LAN cable for internet connectivity due to unavailability of Wifi Module. 
Future Improvements: Adding Wifi module and a Temperature sensor to protect from house fires. Moreover image processing can be employed to judge if the detected intruder is a family member, a pet or a stranger using face detection and human detection algorithms.
Instructions to Run: Boot Raspberry Pi 2 with Raspian. Install SSMTP Install Mutt Install Telegram and configure Install Yowsup Run following commands 'sudo raspi-config' Enable Pi Camera Copy Test.py to Desktop Run following commands 'sudo python Test.py' The system is now active.
