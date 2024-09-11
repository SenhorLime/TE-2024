from GameObject import GameObject
from pygame.locals import *


class Player(GameObject):
    def __init__(self, img):
        super().__init__(img)
        self._rect = self._img.get_rect(x=400, y=530)
        self._vx = self._vx = 0

    def update(self, key) -> None:
        if key.get_pressed()[K_a]:
            self._vx = -10
        elif key.get_pressed()[K_d]:
            self._vx = 10
        else:
            self._vx = 0

        self._rect.x = self._rect.x + self._vx
        self._rect.y = self._rect.y + self._vy
