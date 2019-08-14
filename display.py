import pygame
from pygame.locals import DOUBLEBUF

class Display2D(object):
  def __init__(self, W, H):
    pygame.init()
    self.screen = pygame.display.set_mode((W, H), DOUBLEBUF) #init a screen
    self.surface = pygame.Surface(self.screen.get_size()).convert()
    print(W, H)

  def paint(self, img):
    for event in pygame.event.get():
      pass

    # RGB, not BGR (might have to switch)
    pygame.surfarray.blit_array(self.surface, img.swapaxes(0,1)[:, :, [2,1,0]]) #0,1,2 copy val from arr int o surface
    self.screen.blit(self.surface, (0,0))   #update, top left corener

    # blit
    pygame.display.flip()
