import random
from TransmissionBlock import TransmissionBlock
from Reconstructor import Reconstructor

class NetworkNode:
    def __init__(self, p, g):
        self.p, self.g = p, g

    def generate_private_key(self):
        self.priv_key = random.randint(0, self.p-1)

    def generate_public_key(self):
        self.pub_key = pow(self.g, self.priv_key, self.p)

    def get_public_key(self):
        return self.pub_key, self.p, self.g

    def set_partner_public_key(self, pub_key):
        self.partner_public_key = pub_key

    def compute_routing_array(self, Z, n):
        blocks = [TransmissionBlock(Z, self.priv_key, self.p, self.g, self.pub_key) for i in range(n)]
        return [b.show() for b in blocks]

    def recover_array(self, X, k):
        recon = Reconstructor(*self.partner_public_key, X)
        print("Verified blocks: " + str(recon.verify()))
        rec = recon.recover(k-1)
        return rec