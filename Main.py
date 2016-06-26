import RPi.GPIO as GPIO
import time
import picamera, os
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24
SWITCH = 14

GPIO.setmode(GPIO.BCM)
	
print "Distance Measurement In Progress"
camera = picamera.PiCamera()
camera.vflip = True
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(SWITCH,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

start_time = time.time()
flag = 0
distance = 0
while((time.time()-start_time)<4):
	prev_distance = distance
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
	  pulse_start = time.time()

	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)
	print "Distance:",distance,"cm"
	if(abs(distance- prev_distance) <10):
		prev_distance = distance

avg_dist = prev_distance

while(1):
	if(GPIO.input(SWITCH)==1):
	
	
		prev_distance = distance
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
	
		while GPIO.input(ECHO)==0:
		  pulse_start = time.time()
	
		while GPIO.input(ECHO)==1:
		  pulse_end = time.time()
	
		pulse_duration = pulse_end - pulse_start
	
		distance = pulse_duration * 17150
	
		distance = round(distance, 2)
		print "Distance:",distance,"cm"
		if((prev_distance-distance > 100) & flag):
			
			
			camera.start_recording('vid.h264')
			time.sleep(5)
			camera.stop_recording()
			camera.capture('image1.jpg')
			time.sleep(0.5)
			camera.capture('image2.jpg')
			os.system("sudo mutt -s \'My Mail\' testuser.iot@gmail.com -a image1.jpg image2.jpg vid.h264 < intrusion.txt")
			os.system("cd tg && sudo bin/telegram-cli -k tg-server.pub -w && contact_list && msg Arpit_Jain \"Intrusion Detected!!\"")
			
			#os.popen("msg Arpit_Jain \"Intrusion Detected!!\"","r")
			#os.popen("sudo mpack -s \"Intruder Details\" /home/pi/Desktop/image1.jpg sakshamgupta006@gmail.com" ,"r")
			#os.popen("sudo mpack -s \"Intruder Details\" /home/pi/Desktop/image2.jpg sakshamgupta006@gmail.com","r" )
		
		flag = 1
	if(GPIO.input(SWITCH)==0):
		print ("SWITCH OFF")


GPIO.cleanup()
