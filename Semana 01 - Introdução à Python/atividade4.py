# Simple pygame program
#Import and initialize the pygame library

import pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
runnning = True

while runnning:
  #Did the use click the window close button?
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      runnning = False
      
  # Fill the background with white
  screen.fill((255, 255, 255))
  
  # Draw a solid blue circle in the center
  pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
  
  # Flip the display
  pygame.display.flip()
  
pygame.quit()