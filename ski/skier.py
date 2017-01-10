import pygame, sys, random, time, math, mbevent
import pygame.freetype
pygame.init()

size = width, height = 320,400
black = 0,0,0
cyan = pygame.Color(0,255,255)
white = 255,255,255
speed = 1

screen = pygame.display.set_mode(size)

skier = pygame.image.load("skier.png")
skierrect = skier.get_rect()
skierR = pygame.transform.scale(skier,(int(skierrect.width/10),int(skierrect.height/10)))
skierL = pygame.transform.flip(skierR,True,False)
skierrect = skierR.get_rect()
skierrect.left = width/2 - skierrect.width/2
skierrect.top = 30
skier = skierR

tree = pygame.image.load("fir.png")
treerect = tree.get_rect()
tree = pygame.transform.scale(tree,(30,int(treerect.height/treerect.width*30)))
treerect = tree.get_rect()
trees = []

gem = pygame.image.load("gem.png")
gemrect = gem.get_rect()
gem = pygame.transform.scale(gem,(20,int(gemrect.height/gemrect.width*20)))
gemrect = gem.get_rect()
gems = []
cgems = 0
hgems = 0

font = pygame.freetype.Font(None,size=20)

clock = pygame.time.Clock()

inplay = True

TREEEVENT = pygame.USEREVENT

mbevent.init()

pygame.time.set_timer(TREEEVENT,30)

while 1:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == 276:
                speed = -1
                skier = skierL
            elif event.key == 275:
                speed = 1
                skier = skierR
            elif event.key == 113:
                sys.exit()
            elif event.key == 114:
                trees = []
                gems = []
                cgems = 0
                inplay = True
        if event.type == TREEEVENT:
            if inplay:
                for t in trees:
                    t.move_ip(0,-1)
                for g in gems:
                    g.move_ip(0,-1)
        if event.type == mbevent.MICROBITEVENT:
            speed = math.copysign(1,event.x)
            

    if inplay:
        skierrect.left += speed
        skierrect.left = min(width - skierrect.width,max(0,skierrect.left))

        ntrees = []
        for t in trees:
            if t.top > - treerect.height:
                ntrees.append(t)
        trees = ntrees
        
        for t in trees:
            if skierrect.collidepoint(t.left+t.width/2,t.top+t.height):
                inplay = False

        if not inplay:
            hgems = max(cgems,hgems)

        ngems = []

        for g in gems:
            if skierrect.collidepoint(g.left+g.width/2,g.top+g.height/2):
                cgems += 1
            elif g.top > -gemrect.height:
                ngems.append(g)
        gems = ngems
                
        
        if random.random() > .99:
            r = treerect.copy()
            r.left = random.randint(treerect.width,width-treerect.width)
            r.top = height
            trees.append(r)
        if random.random() > .99:
            r = gemrect.copy()
            r.left = random.randint(gemrect.width,width-gemrect.width)
            r.top = height
            gems.append(r)

    screen.fill(white)
    for t in trees:
        screen.blit(tree,t)
    for g in gems:
        screen.blit(gem,g)
    screen.blit(skier,skierrect)
    font.render_to(screen,(20,10),str(cgems),fgcolor=cyan)
    font.render_to(screen,(width - 30,10),str(hgems),fgcolor=cyan)
    pygame.display.flip()
