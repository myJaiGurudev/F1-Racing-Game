import pygame
import time
import random
import os
pygame.init()
grey=(118,119,110)
red=(245,50,0)
white=(255, 255, 255)
por=(255,0,0)
rd=(255, 120, 0)
black=(100,0,0)
yellow=(255,200,0)
clock=pygame.time.Clock()
display=pygame.display.set_mode((1000,600))
pygame.display.set_caption("F1 Racing Game")
carimg=pygame.image.load("car1.png")
carimg=pygame.transform.scale(carimg,(27,60))
bgleft=pygame.image.load("left.png")
bgright=pygame.image.load("right.png")
width=23
fnt=pygame.font.SysFont("Algerian", 70)
font=pygame.font.SysFont("Algerian", 50)
fot=pygame.font.SysFont("Times New Roman", 70)
def welcome():
    pygame.mixer.music.load('gamestart.mp3')
    pygame.mixer.music.play()
    exit_game=False
    while not exit_game:
        bgim=pygame.image.load("bj.jpg")
        bgim=pygame.transform.scale(bgim, (1000, 600))
        display.blit(bgim, (0, 0))
        text_screen("Made  By:  Anurag  Singh", yellow, 200, 530)
        textcreen("F1  Racing  Game !", rd, 200, 40)
        text_screen("Jai Guru Dev", white, 350, 150)
        text_screen("Press  Space  Bar  To  Play.", por, 180, 450)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    loop()
            pygame.display.update()
            clock.tick(60)
def policecar(p_x,p_y,police):
    if police==0:
        p_come=pygame.image.load("car2.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    if police==1:
        p_come=pygame.image.load("car3.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    if police==2:
        p_come=pygame.image.load("car1.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    display.blit(p_come,(p_x,p_y))
def pocar(a,b,police):
    if police==0:
        p_come=pygame.image.load("car3.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    if police==1:
        p_come=pygame.image.load("car1.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    if police==2:
        p_come=pygame.image.load("car2.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    display.blit(p_come,(a,b))
def pulice(m,l,police):
    if police==0:
        p_come=pygame.image.load("car1.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    if police==1:
        p_come=pygame.image.load("car2.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    if police==2:
        p_come=pygame.image.load("car3.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    display.blit(p_come,(m,l))
def pcar(p,q,police):
    if police==0:
        p_come=pygame.image.load("car1.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    if police==1:
        p_come=pygame.image.load("car2.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    if police==2:
        p_come=pygame.image.load("car3.png")
        p_come=pygame.transform.scale(p_come,(27,60))
    display.blit(p_come,(p,q))
def textcreen(text, color, a, b):
    screen_text=fnt.render(text, True, color)
    display.blit(screen_text, [a,b])
def text_screen(text, color, a, b):
    screen_text=font.render(text, True, color)
    display.blit(screen_text, [a,b])
def textscreen(text, color, a, b):
    screen_text=fot.render(text, True, color)
    display.blit(screen_text, [a,b])
def text_object(text,font):
    b=font.render(text,True,color)
    return b,b.get_rect()
def bg():
    display.blit(bgleft,(0,0))
    display.blit(bgright,(850,0))
def car(x,y):
    display.blit(carimg,(x,y))
def loop():
    pygame.mixer.music.load('back.mp3')
    pygame.mixer.music.play()
    exit_game=False
    game_over=False
    x=450
    x_c=0
    vel=13
    fps=60
    score=0
    police=0
    m=random.randrange(600,(750-width))
    a=random.randrange(130,(250-width))
    b=600
    l=600
    p_x=random.randrange(240,(400-width))
    p=random.randrange(400,(600-width))
    q=600
    p_y=600
    p_width=23
    p_height=47
    y_c=-3
    y=500
    if(not os.path.exists("hscore.txt")):
        with open("hscore.txt", "w") as f:
            f.write("0")
    with open("hscore.txt", "r") as f:
            hiscore=f.read()
    while not exit_game:
        if game_over:
            with open("hscore.txt", "w") as f:
                f.write(str(hiscore))
            display.fill(white)
            bgim=pygame.image.load("crash.jpg")
            bgim=pygame.transform.scale(bgim, (1000, 700))
            display.blit(bgim, (0, 0))
            if score==int(hiscore):
                text_screen("Nice !  You  made  a  Hiscore :"+str(hiscore)+"", rd, 120, 100)
            textscreen("Score:"+str(score)+"   Hiscore:"+str(hiscore)+"", yellow, 10, 10)
            textcreen("Car  Crashed !", por, 250, 250)
            textscreen("Press  enter  to  continue.", rd, 200, 400)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        loop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_c=-6
                        y_c=0
                    if event.key==pygame.K_RIGHT:
                        x_c=6
                        y_c=0
                    if event.key==pygame.K_UP:
                        y_c=-5
                        x_c=0
                    if event.key==pygame.K_DOWN:
                        y_c=5
                        x_c=0
            x+=x_c
            y+=y_c
            display.fill(grey)
            bg()
            l-=(vel/5)
            q-=(vel/3)
            b-=(vel/5)
            p_y-=(vel/4)
            policecar(p_x,p_y,police)
            p_y+=vel
            l+=vel+2
            b+=vel+2
            q+=vel+1
            pocar(a,b,police)
            pcar(p,q,police)
            pulice(m,l,police)
            car(x,y)
            if x<130 or x>850-width or y<0 or y>600:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            if p_y>600:
                score+=1
                if score>int(hiscore):
                    hiscore=score
                p_y=0-p_height
                p_x=random.randrange(130,250)
                police=random.randrange(0,2)
            if y<p_y+p_height:
                if x>p_x and x<p_x+p_width or width>p_x and x+width<p_x+p_width:
                    game_over=True
                    pygame.mixer.music.load('gameover.mp3')
                    pygame.mixer.music.play()
            if b>600:
                score+=1
                if score>int(hiscore):
                    hiscore=score
                b=0-p_height
                a=random.randrange(240,450)
                police=random.randrange(0,2)
            if y<b+p_height:
                if x>a and x<a+p_width or width>a and x+width<a+p_width:
                    game_over=True
                    pygame.mixer.music.load('gameover.mp3')
                    pygame.mixer.music.play()
            if q>600:
                score+=1
                if score>int(hiscore):
                    hiscore=score
                q=0-p_height
                p=random.randrange(400,650)
                police=random.randrange(0,2)
            if y<q+p_height:
                if x>p and x<p+p_width or width>p and x+width<p+p_width:
                    game_over=True
                    pygame.mixer.music.load('gameover.mp3')
                    pygame.mixer.music.play()
            if l>600:
                score+=1
                if score>int(hiscore):
                    hiscore=score
                l=0-p_height
                m=random.randrange(600,800)
                police=random.randrange(0,2)
            if y<l+p_height:
                if x>m and x<m+p_width or width>m and x+width<m+p_width:
                    game_over=True
                    pygame.mixer.music.load('gameover.mp3')
                    pygame.mixer.music.play()
            text_screen("Score:"+str(score)+"   Hiscore:"+str(hiscore)+"", yellow, 5, 5)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()

