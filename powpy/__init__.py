from re import match
from random import choice, randrange, getrandbits
import hashlib

def make_hash(text):
    '''
    Convert a string into a MD5 hash
    '''
    m = hashlib.md5()
    m.update(text.encode("utf_8"))
    return str(m.hexdigest())

def random_hash():
    '''
    Generate a random MD5 hash
    '''
    return getrandbits(128)# :P Thanks to --> http://stackoverflow.com/questions/976577/ddg#976607

def proof_of_work(initial, difficult):
    '''
    Do a proof of work, using MD5 hashes.
    INPUT: An initial hash and a difficult
    OUTPUT: A new hash, depending of initial hash
    '''
    work = random_hash()
    while True:
        while not( match("0"*difficult, make_hash(initial + work)) ):# Repeats until find a valid hash
            # Modify the munber of zeros to make the POW easier or harder
            work = random_hash()
        return work# Once the hash matches the requirements