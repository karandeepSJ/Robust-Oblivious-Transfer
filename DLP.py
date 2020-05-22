import Crypto.Util, Crypto.Random
import math

class DLP:
    def __init__(self):
        self.p = self.generatePrimeOfGivenLength(8)
        self.g = self.findGenerator(self.p)

    def getAllPrimes(self, n):
        res = []
        for i in range(2,n):
            if all(i%j!=0 for j in range(2,int(math.sqrt(i))+1)):
               res.append(i)
        return res

    def generatePrimeOfGivenLength(self, n):
        return Crypto.Util.number.getPrime(n)

    def is_generator(self, h, q_f, p):
        flag = 0
        for q_i in q_f:
            if (h ** q_i) % p == 1:
                flag = 1
                break
        if flag==0:
            return True
        else:
            return False

    def findGenerator(self, p):
        primes = self.getAllPrimes(p-1)
        q = p-1
        q_f = [q//prime for prime in primes if q % prime == 0]
        for h in range(1, q):
            if not self.is_generator(h, q_f, p):
                pass
            else:
                return h

    def get_params(self):
        return self.p, self.g