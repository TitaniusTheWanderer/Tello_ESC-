from djitellopy import tello
from time import sleep


tello = tello.Tello

tello.connect()

# go get battery

print(tello.get_battery())

#take off

tello.takeoff()

#move to correct high

tello.move_up(100)

#move forward

tello.move_forward(500)

tello.move_forward(200)

#turn left(counter clockwise)

tello.rotate_counter_clockwise(90)

#move forward(again yeah)


tello.move_forward(350)

#we do a little reverse

tello.move_back(350)

#turn right(clockwise)

tello.rotate_clockwise(90)

#a weee bit more turning

tello.move_back(500)

tello.move_back(200)

#and done

tello.land
