import pygame


class GameObject:
    def __init__(self, img):
        self._img = img
        self._rect = None
        self._vx = 0
        self._vy = 0

    def __str__(self) -> str:
        return f"XY({self._rect.x},{self._rect.y}); VxVy({self._vx},{self._vy})"

    def getRect(self):
        return self._rect
    
    def update(self, dt=1):
        self._rect.y = self._rect.y + self._vx * dt

    def draw(self, panel):
        panel.blit(self._img, self._rect)
        color = (255, 0, 0)
        pygame.draw.rect(panel, color, self._rect, width=1)
