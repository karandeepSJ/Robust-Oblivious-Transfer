import random 
from Signer import Signer

class TransmissionBlock(Signer):
    def __init__(self, coef, priv_key, p, g, y):
        self.x = random.randint(0, p-1)
        self.val = self.polynomial(coef, self.x)
        super().__init__(priv_key, p, g, y)
        self.sign = self.sgn()

    def polynomial(self, coef, x):
        total = 0
        for a in reversed(coef):
            total = (total*x + a)
        return total

    def show(self):
        return (self.x, self.val, self.sign)

    def sgn(self):
        return super().signature(self.val)

    def corrupt(self):
        self.val=self.val+random.randint(1, 10000)