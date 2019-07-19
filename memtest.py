import string
import random
import sys
import os
import _thread
import hashlib

def hash(plainString):
    hash_object = hashlib.sha512(str.encode(plainString))
    hex_dig = hash_object.hexdigest()
    return str(hex_dig)

def randomString(length):
    rstring = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    encString = hash(hash(hash(hash(hash(hash(hash(rstring)))))))
    return encString

def buildsarray():
    stringsize = random.randint(10000000,20000001)
    newString = randomString(stringsize)
    stringlist.append(newString)
    uString = os.urandom(16)
    stringlist.append(uString)

loop = True
stringlist = []
i = 0
while (loop):
    _thread.start_new_thread(buildsarray, ())
    i = i + 1
    sys.stdout.write("\r%i threads so far" % i)
    sys.stdout.flush()