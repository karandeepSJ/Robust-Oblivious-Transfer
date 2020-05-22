from NetworkNode import NetworkNode

class Server(NetworkNode):
    def __init__(self, p, g):
        super().__init__(p, g)

    def el_gamal_decrypt(self, ciphertext):
        c2 = ciphertext
        s = pow(self.partner_public_key[0], self.priv_key, self.p)
        m = (pow(s, self.p - 2, self.p) * c2) % self.p
        return m

    def decrypt_message(self, Z):
        self.Y = []
        for i in range(len(Z)):
            self.Y.append(self.el_gamal_decrypt(Z[i]))

    def send_encrypted_data(self, data):
        to_send = []
        for i in range(len(data)):
            to_send.append(data[i]^self.Y[i])

        return to_send