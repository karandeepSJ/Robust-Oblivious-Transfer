from Verifier import Verifier
from numpy.polynomial import polynomial as Pl
import numpy as np

class Reconstructor(Verifier):
    def __init__(self, y, p, g, blocks):
        self.blocks = blocks
        super().__init__(y, p, g)

    def verify(self):
        self.status = []
        for b in self.blocks:
            self.status.append(super().verify(b[2], b[1]))
        return self.status

    def recover(self, deg):
        X = np.array([self.blocks[i][0] for i in range(len(self.blocks)) if self.status[i]])
        Y = np.array([self.blocks[i][1] for i in range(len(self.blocks)) if self.status[i]])
        Y = Y.astype('float')
        coef = Pl.polyfit(X, Y, deg)
        return np.round(coef).astype(int).tolist()
