import random

class Signer:
    def __init__(self, priv_key, p, g, y):
        self.priv_key = priv_key
        self.p = p
        self.g = g
        self.y = y

    def CRHF(self, x1, x2, x3):
        k1 = 2
        k2 = 3
        z = pow(self.g, k1, self.p)
        z1 = pow(self.g, k2, self.p)

        return (pow(self.g, x1, self.p) * pow(z, x2, self.p) * pow(z1, x3, self.p)) % self.p

    def signature(self, m):
        r = random.randint(0, self.p - 1)
        a1 = pow(m, self.priv_key, self.p)
        a2 = pow(m, r, self.p)
        a3 = pow(self.g, r, self.p)
        c = self.CRHF(a1, a2, a3)
        s = c * self.priv_key + r
        return [s, a1, a2, a3]