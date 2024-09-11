from random import randint

from GameObject import GameObject


class Bola(GameObject):
    def __init__(self, img, windowWidth, x, y):
        super().__init__(img)
        x = x if x > 0 else randint(0, windowWidth - img.get_width())
        y = y if y > 0 else 0 - img.get_height()

        self._rect = self._img.get_rect(x=x, y=y)

        self._vx = self._vy = randint(2, 3)
        self.isLive = True
