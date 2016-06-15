import pygame,math,sys,os
from pygame.locals import *
#zum ausfuehren von shell skripten
import subprocess
import platform

###Initialisierung

#OS check + directory

dist, ver, name = platform.dist()
#dist enthaelt LinuxMint oder Raspbian
verzeichnis = os.getcwd()
img_verzeichnis = verzeichnis + "/images"
shell_verzeichnis = verzeichnis + '/shell'
java_verzeichnis = verzeichnis + '/java'

print verzeichnis


background_jpg = img_verzeichnis+'/background.jpg'
button_png = img_verzeichnis+'/button.png'
button_on_png = img_verzeichnis+'/button_on.png'
w_button_png = img_verzeichnis+'/weather.png'
w_button_on_png =img_verzeichnis+'/weather_on.png'
black_jpg = img_verzeichnis+'/black.jpg'
p_button_png = img_verzeichnis+'/ping.png'
p_button_on_png = img_verzeichnis+'/ping_on.png'

if dist == "LinuxMint":
    screen = pygame.display.set_mode((800,480))
else:
    screen = pygame.display.set_mode((800,480),FULLSCREEN)

background = pygame.image.load(background_jpg)
background = pygame.transform.scale(background, (800,480))
black = pygame.image.load(black_jpg)
button1_on = pygame.image.load(button_on_png)
button1_off = pygame.image.load(button_png)
button2_on = pygame.image.load(button_on_png)
button2_off = pygame.image.load(button_png)
button3_on = pygame.image.load(button_on_png)
button3_off = pygame.image.load(button_png)
w_button_on = pygame.image.load(w_button_on_png)
w_button_off = pygame.image.load(w_button_png)
p_button_on = pygame.image.load(p_button_on_png)
p_button_off = pygame.image.load(p_button_png)

#initialisiert font
pygame.font.init()

##Buttons

#state
button_1_state = False
button_2_state = False
button_3_state = False
w_button_state = False
p_button_state = False

#psition
button_y = 150
button_1_x = 200
button_2_x = 350
button_3_x = 500

w_button_y = 420
w_button_x = 740

p_button_y = 420
p_button_x = 10

##Labels
label_h = button_y + 110
gray = (60,60,60)
myfont = pygame.font.SysFont("Comic Sans MS", 35)
label1 = myfont.render("Desk", 1, gray)
label2 = myfont.render("Funzel", 1, gray)
label3 = myfont.render("Room", 1, gray)

##Counter
sleepcount = 0
pingcount = 0

###Defining

#Screen
def update_screen():
    print ("Update")
    global screen,background, black
    global button1_on,button1_off
    global button2_on,button2_off
    global button3_on,button3_off
    global p_button_on,p_button_off
    global w_button_on,w_button_off
    global label1,label2,label3

    screen.blit(background,(0,0))

    if button_1_state:
        screen.blit(button1_on,(button_1_x,button_y))
    else:
        screen.blit(button1_off,(button_1_x,button_y))

    if button_2_state:
        screen.blit(button2_on,(button_2_x,button_y))
    else:
        screen.blit(button2_off,(button_2_x,button_y))

    if button_3_state:
        screen.blit(button3_on,(button_3_x,button_y))
    else:
        screen.blit(button3_off,(button_3_x,button_y))

    if w_button_state:
        screen.blit(w_button_on,(w_button_x,w_button_y))
    else:
        screen.blit(w_button_off,(w_button_x,w_button_y))

    if p_button_state:
        screen.blit(p_button_on,(p_button_x,p_button_y))
    else:
        screen.blit(p_button_off,(p_button_x,p_button_y))

    screen.blit(label1, (220, label_h))
    screen.blit(label2, (365, label_h))
    screen.blit(label3, (525, label_h))

    pygame.display.update()

#Black Screen
def black_screen():
    global black
    screen.blit(black,(0,0))
    pygame.display.update()

#Ping Automation
def ping():
    global button_1_state,button_2_state,button_3_state
    subprocess.call("sudo ping -c 3 -w 1 192.168.178.29 > pinglog.txt",shell = True)
    # Open .txt and grap for "ms"
    pingfile = open("pinglog.txt",'r')
    log = pingfile.read()
    pingfile.close()
    if log.find("3 received") <= 0 or log.find("2 received") <= 0 or log.find("1 received") <= 0: #teste ob der ping empfangen wurde
        #Lampen auschalten auch wenn sie durch die App angeschaltet wurden
        if button_1_state:
            button_1_click()
        else:
            if dist != "LinuxMint":
                subprocess.call("cd && sudo raspberry-remote/send 10101 1 0",shell = True)
        if button_2_state:
            button_2_click()
        else:
            if dist != "LinuxMint":
                subprocess.call("cd && sudo raspberry-remote/send 10101 2 0",shell = True)
        if button_3_state:
            button_3_click()
        else:
            if dist != "LinuxMint":
                subprocess.call("cd && sudo raspberry-remote/send 10101 3 0",shell = True)

#Buttons
def button_1_click():
    global button_1_state, dist
    button_1_state = not button_1_state
    update_screen()
    if dist != "LinuxMint":
        if button_1_state:
            subprocess.call("cd && sudo raspberry-remote/send 10101 1 1",shell = True)
        else:
            subprocess.call("cd && sudo raspberry-remote/send 10101 1 0",shell = True)


def button_2_click():
    global button_2_state
    button_2_state = not button_2_state
    update_screen()
    if dist != "LinuxMint":
        if button_2_state:
            subprocess.call("cd && sudo raspberry-remote/send 10101 2 1",shell = True)
        else:
            subprocess.call("cd && sudo raspberry-remote/send 10101 2 0",shell = True)

def button_3_click():
    global button_3_state
    button_3_state = not button_3_state
    update_screen()
    if dist != "LinuxMint":
        if button_3_state:
            subprocess.call("cd && sudo raspberry-remote/send 10101 3 1",shell = True)
        else:
            subprocess.call("cd && sudo raspberry-remote/send 10101 3 0",shell = True)

def w_button_click():
    global w_button_state, button_y, label_h
    w_button_state = not w_button_state
    update_screen()
    for anim in range(8):
        if w_button_state:
            button_y -= 17
        else:
            button_y += 17
        label_h = button_y + 110
        update_screen()

def p_button_click():
    global p_button_state,pingcount
    pingcount = 0
    p_button_state = not p_button_state
    update_screen()





#Collision
def collision(x,y):
    if x > button_1_x and x < button_1_x+100 and y > button_y and y < button_y+100:
        button_1_click()
    if x > button_2_x and x < button_2_x+100 and y > button_y and y < button_y+100:
        button_2_click()
    if x > button_3_x and x < button_3_x+100 and y > button_y and y < button_y+100:
        button_3_click()
    if x > w_button_x and x < w_button_x + 50 and y > w_button_y and y < w_button_y+50:
        w_button_click()
    if x > p_button_x and x < p_button_x + 50 and y > p_button_y and y < p_button_y+50:
        p_button_click()
###Instalation

update_screen()

clock = pygame.time.Clock() #clock for framerate
switch = True

###Main loop

while switch:
    #user input
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            update_screen()
            sleepcount = 0
            x,y = pygame.mouse.get_pos()
            collision(x,y)
            print(x,y)
        if not hasattr(event, 'key'): continue
        if event.key == K_q :
            print ("Quit")
            switch = False
    if sleepcount == 3000:
        black_screen()
    if pingcount == 100 and not p_button_state:
        ping()
        pingcount = 0
        print "ping"
    sleepcount += 1
    if not p_button_state:
        pingcount += 1
pygame.quit()
sys.exit() #quit
