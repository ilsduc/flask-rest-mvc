import hashlib
import random
import time

class Hash:

    @classmethod
    def create (that):
        randomValue = time.time()+random.randint(1000000, 10000000)
        return hashlib.sha1(str(randomValue).encode('utf-8')).hexdigest()

    @classmethod
    def create_from (that, value):
        return hashlib.sha1(str(value).encode('utf-8')).hexdigest()
