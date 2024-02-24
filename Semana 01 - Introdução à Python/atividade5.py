# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame.locals import *
from random import randint



pygame.init()

lastTime = 0
objctsOut = 0


# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

dropImg = pygame.image.load("assets\\droplet.png").convert_alpha()
bucketImg = pygame.image.load("assets\\bucket.png").convert_alpha()
fundoImg = pygame.image.load("assets\\fundo.png").convert_alpha()


musica_de_fundo = pygame.mixer.music.load('assets\\rain.ogg')
barulho_colisao = pygame.mixer.Sound('assets\\drop.ogg')

font = pygame.font.SysFont("assets\\x-files.ttf", 32)


class Player:   
    def __init__(self, img):
        x = 400
        y = 530        
        #self.img = pygame.transform.scale(img, (32,32))        
        self.img = img
        self.rect = self.img.get_rect(x=x,y=y)
        self.vx = self.vy = 0

    def __str__(self):
        return f"XY({self.rect.x},{self.rect.y}); VxVy({self.vx},{self.vy})"
    
    
    def update(self, key, dt=1 ):
        
        if key.get_pressed()[K_a]:
            self.vx = -10                    
        elif key.get_pressed()[K_d]:
            self.vx = 10
        else:
            self.vx = 0
        
        '''if key.get_pressed()[K_w]:
            self.vy = -5        
        elif key.get_pressed()[K_s]:
            self.vy = 5
        else:
            self.vy = 0
        '''
        self.rect.x = self.rect.x + self.vx       
        self.rect.y = self.rect.y + self.vy
        

    def draw(self, panel):               
        panel.blit(self.img, self.rect)
        color = (255,0,0 )
        pygame.draw.rect(screen,color, self.rect, width=1)

class Bola:      
    def __init__(self, x, y, img):
        x = x if x > 0 else randint(0,screen.get_width()-img.get_width())
        y = y if y > 0 else 0 - img.get_height();
        #self.img = pygame.transform.scale(img, (32,32))        
        self.img = img
        self.rect = self.img.get_rect(x=x,y=y)
        self.vx = self.vy = randint(2, 3)
        self.isLive = True

    def __str__(self):
        return f"XY({self.rect.x},{self.rect.y}); VxVy({self.vx},{self.vy})"
    
    def update(self, dt=1):               
        self.rect.y = self.rect.y + self.vy*dt                

    def draw(self, panel):               
        panel.blit(self.img, self.rect)
        color = (255,255,0 )
        pygame.draw.rect(screen,color, self.rect, width=1)

bols = []


player = Player(bucketImg)

def creatObject(x=0, y=0):
    b1 = Bola(x,y,dropImg)
    bols.append(b1)    
    global lastTime      
    lastTime = pygame.time.get_ticks()
    
    



clock = pygame.time.Clock()

pygame.display.set_caption('Rain game')
pygame.display.set_icon(dropImg)


current_time = pygame.time.get_ticks()

# Run until the user asks to quit
running = True
pygame.mixer.music.play(-1)
creatObject()
while running:    
    #Pega entrada
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:          
            #bols.append(Bola(event.pos[0],event.pos[1],imp))                             
            creatObject(event.pos[0],event.pos[1])

       
    #update world
    for bol in bols:
        bol.update()        
        if (bol.rect.y > screen.get_height()) :            
            bols.remove(bol)            
            #objctsOut+=1
        elif (not bol.isLive):
            bols.remove(bol)            
            objctsOut+=1
    
    player.update(pygame.key)
    
    text = font.render(str(objctsOut) , True,(0,0,255))    
    
    currentTime = pygame.time.get_ticks()    
    if ( currentTime -lastTime) > 1000:
        creatObject()
        
    

    #Desenha o mundo.

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), ( b1.x,b1.y), 20)
    # Using blit to copy content from one surface to other
    
    # Fill the background with white            
    #screen.fill((255,255, 255))
    screen.blit(fundoImg, (0,0))    
    
    for bol in bols:
        bol.draw(screen)        

        if bol.rect.colliderect(player.rect):
            bol.isLive = False
            barulho_colisao.play()

    player.draw(screen)

    screen.blit(text, (740, 20))
    screen.blit(  font.render( str(currentTime) , True,(0,0,255)), (700, 40))
    screen.blit(  font.render( str(lastTime) , True,(0,0,255)), (700, 60))
    screen.blit(  font.render( str(currentTime- lastTime) , True,(0,0,255)), (700, 80))
    
    # Flip the display
    pygame.display.flip()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()