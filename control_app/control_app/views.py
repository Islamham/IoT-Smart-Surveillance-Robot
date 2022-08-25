#imports
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
import picar
import os
from time import sleep
from django.shortcuts import render
from django.http import HttpResponse

picar.setup() #setup picar variables

FW_CENTRE = 110 #centre angle for front wheels
TILT_ANGLE_CENTRE = 70 #centre angle for tilt
PAN_ANGLE_CENTRE = 70 #centre angle for pan

PAN_ANGLE_MAX   = PAN_ANGLE_CENTRE + 40 #pan left
PAN_ANGLE_MIN   = PAN_ANGLE_CENTRE - 40 #pan right
TILT_ANGLE_MAX  = TILT_ANGLE_CENTRE + 30 #tilt up
TILT_ANGLE_MIN  = TILT_ANGLE_CENTRE - 30 #tilt down
FW_ANGLE_MAX    = FW_CENTRE+40 #turn left
FW_ANGLE_MIN    = FW_CENTRE-40 #turn right

bw = back_wheels.Back_Wheels() #initialize back wheels
fw = front_wheels.Front_Wheels() #initialize front wheels
pan_servo = Servo.Servo(1) #initialize camera pan servo
tilt_servo = Servo.Servo(2) #initialize camera tilt servo
picar.setup() #setup picar variables

bw.speed = 0 #set initial speed to no speed
fw.turn(FW_CENTRE) #initialize front wheels to be straight
pan_servo.write(PAN_ANGLE_CENTRE) #pan camera to middle angle
tilt_servo.write(TILT_ANGLE_CENTRE) #tilt camera to middle angle

motor_speed = 60 #active speed variable

def home(request): #when in home url (no extension)
    return render(request, "control_website.html") #setup website

def turn_left(request): #when url has turn_left extension
    fw.turn(FW_ANGLE_MIN) #turn front wheels to the left
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") #remove the extension and reload homepage

def turn_right(request): #when url has turn_right extension
    fw.turn(FW_ANGLE_MAX) #turn front wheels to the right
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") #remove the extension and reload homepage

def drive_forward(request): #when url has drive_forward extension
    bw.speed = motor_speed #set speed to active speed
    bw.backward() #make back wheen run forward (the engines are backwards so the functions are also backwards)
    fw.turn(FW_CENTRE) #reset the front wheels to straight
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") #remove the extension and reload homepage

def drive_backward(request): #when url has the drive_backward extension
    bw.speed = motor_speed #set speed to active speed
    bw.forward() #make back wheen run backward (the engines are backwards so the functions are also backwards)
    fw.turn(FW_CENTRE) #reset the front wheels to straight
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") #remove the extension and reload homepage

def drive_stop(request): #when url has drive_stop extension
    bw.speed = 0 #set speed to 0
    bw.stop() #stop the back wheels
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") #remove the extension and reload homepage

def tilt_up(request): #when url has tilt_up extension
    tilt_servo.write(TILT_ANGLE_MAX) #tilt camera upwards
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") #remove the extension and reload homepage

def tilt_down(request): #when url has tilt_down extension
    tilt_servo.write(TILT_ANGLE_MIN) #tilt camera downwards
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") #remove the extension and reload homepage

def pan_left(request): #when url has pan_left extension
    pan_servo.write(PAN_ANGLE_MAX) #pan camera left
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") #remove the extension and reload homepage

def pan_right(request): #when url has pan_right extension
    pan_servo.write(PAN_ANGLE_MIN) #pan camera right 
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") #remove the extension and reload homepage

def cam_reset(request): #when the url has the cam_reset extension
    pan_servo.write(PAN_ANGLE_CENTRE) #reset pan angle
    tilt_servo.write(TILT_ANGLE_CENTRE) #reset tilt angle
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") #remove the extension and reload homepage



#def main():
#    turn_straight()
#    sleep(3)
#    turn_left()
#    sleep(3)
#    turn_straight()
#    sleep(3)
#    turn_right()
#    sleep(3)
#    turn_straight()
#    sleep(3)
#    drive_forward()
#    sleep(3)
#    drive_stop()
#    sleep(3)
#    drive_backward()
#    sleep(3)
#    drive_stop()
#
#
#if __name__ == "__main__":
#    main()





#def main():
#    turn_straight()
#    sleep(3)
#    turn_left()
#    sleep(3)
#    turn_straight()
#    sleep(3)
#    turn_right()
#    sleep(3)
#    turn_straight()
#    sleep(3)
#    drive_forward()
#    sleep(3)
#    drive_stop()
#    sleep(3)
#    drive_backward()
#    sleep(3)
#    drive_stop()
#
#
#if __name__ == "__main__":
#    main()



