import random
import string

class PasswordGen:
    def __init__(self, length):
        if length > 94 or length < 4:
            self.length = 10
        else:
            self.length = length

    def generate(self):
        all = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.sample(all,self.length))
        return password

