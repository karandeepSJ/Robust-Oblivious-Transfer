class Verifier:
    def __init__(self, y, p, g):
        self.y = y
        self.p = p
        self.g = g

    def CRHF(self, x1, x2, x3):
        k1 = 2
        k2 = 3
        z = pow(self.g, k1, self.p)
        z1 = pow(self.g, k2, self.p)

        return (pow(self.g, x1, self.p) * pow(z, x2, self.p) * pow(z1, x3, self.p)) % self.p

    def verify(self, m, v):
        c = self.CRHF(m[1], m[2], m[3])
        s = m[0]

        cond1 = (pow(self.g, s, self.p) == (pow(self.y, c, self.p) * m[3]) % self.p)
        cond2 = (pow(v, s, self.p) == (pow(m[1],c, self.p) * m[2]) % self.p)
        if cond1 and cond2:
            return True
        else:
            return False