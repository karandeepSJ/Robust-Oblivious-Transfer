from NetworkNode import NetworkNode
import random

class Client(NetworkNode):
    def __init__(self, p, g):
        super().__init__(p, g)

    def gen_random_numbers(self, k):
        ret = []
        for i in range(k):
            ret.append(random.randint(0,self.p-1))
        return ret

    def el_gamal_encrypt(self, m):
        h, p, g = self.partner_public_key
        s = pow(h, self.priv_key, p)
        c2 = (m * s) % p
        return c2

    def set_index(self, idx):
        self.idx = idx

    def generate_message_to_server(self, k):
        Z = self.gen_random_numbers(k)
        self.R = Z.copy()
        Z[self.idx] = self.el_gamal_encrypt(Z[self.idx])
        return Z

    def extract_block(self, data):
        b = data[self.idx] ^ self.R[self.idx]
        return b