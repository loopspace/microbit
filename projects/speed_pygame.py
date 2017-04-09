import pygame, sys, random, time, math, mbhandler
import pygame.freetype
pygame.init()

modes = sorted(pygame.display.list_modes(), key=lambda t: t[0], reverse=True)
size = modes[0]
width, height = size

black = 0,0,0
cyan = pygame.Color(0,255,255)
white = 255,255,255
red = 255,0,0
green = 0,255,0
speed = 1

msgfont = pygame.freetype.SysFont("TeX Gyre Pagella",size=height//20)
titlefont = pygame.freetype.SysFont("TeX Gyre Pagella",size=height//15)
splashfont = pygame.freetype.SysFont("TeX Gyre Pagella",size=height//5)

mlh = msgfont.get_sized_height() + 2
tlh = titlefont.get_sized_height() + 2
slh = splashfont.get_sized_height() + 2

msgfont.origin = True
titlefont.origin = True
splashfont.origin = True

screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
times = []

mbhandler.init(method="pygame", output="raw")

scores = {}

# Game states:
# 0: Wait for a click to start
# 1: Started, but trigger not given
# 2: Trigger given
gameState = 0

# Game levels:
# 0: Easy, don't subtract if early
# 1: Hard, early means minus points
gameLevel = 0

disqualified = []

message = ["Click to start","q to quit","r to restart"]
splash = ""

TRIGGEREVENT = pygame.USEREVENT
pygame.USEREVENT += 1

dTime = 0

def closedown():
    for t in times:
        print("{}, {}".format(t[0],t[1]))
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closedown()
        if event.type == pygame.KEYDOWN:
            if event.key == 113:
                closedown()
            elif event.key == 114:
                gameState = 0
                message = ["Click to start"]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gameState == 0 and event.button == 1:
                pygame.time.set_timer(TRIGGEREVENT,random.randint(2,5)*1000)
                gameState = 1
                splash = "Wait ..."
                message = ["r to restart, q to quit"]
                disqualified = []
        if event.type == TRIGGEREVENT:
            pygame.time.set_timer(TRIGGEREVENT,0)
            if gameState == 1:
                gameState = 2
                splash = "Go for it!"
                dTime = pygame.time.get_ticks()
        if event.type == mbhandler.MICROBITEVENT:
            mb = event.message
            if not mb in disqualified:
                if gameState == 0:
                    pass
                elif gameState == 1:
                    message = ["{} disqualified".format(mb)]
                    disqualified.append(mb)
                    if gameLevel == 1:
                        if mb in scores:
                            if scores[mb] > 0:
                                scores[mb] -= 1
                elif gameState == 2:
                    splash = mb
                    times.append([mb,pygame.time.get_ticks() - dTime])
                    message = ["Click for next round","{}ms".format(pygame.time.get_ticks() - dTime)]
                    if mb in scores:
                        scores[mb] += 1
                    else:
                        scores[mb] = 1
                    gameState = 0

    if gameState == 0:
        screen.fill(white)
    elif gameState == 1:
        screen.fill(red)
    elif gameState == 2:
        screen.fill(green)

    if not splash == "":
        sr = splashfont.get_rect(splash)
        splashfont.render_to(screen,(width/2 - sr.width/2,height/2 + sr.height/2),splash,fgcolor=black)

    y = 1
    sorted_scores = sorted(scores.items(), key=lambda t: t[1], reverse=True)
    titlefont.render_to(screen,(20,tlh),"Scores:",fgcolor=black)
    for k in sorted_scores:
        y += 1
        msgfont.render_to(screen,(20,mlh*y),"{} {}".format(k[1], k[0]),fgcolor=black)
    y = 0
    for m in reversed(message):
        y += 1
        msgfont.render_to(screen,(20,height-mlh*y),m,fgcolor=black)

    pygame.display.flip()
