from base64 import b64encode, b64decode
import pickle
import requests
import libnum
import hashlib
import sys

try:
    msg1 = "cocotudoispayerbordel"
    h1 = int(hashlib.sha256(msg1.encode()).hexdigest(),base=16)
    msg2 = "starfoullah"
    h2 = int(hashlib.sha256(msg2.encode()).hexdigest(),base=16)
    r = requests.post('http://192.168.120.11:48407/sign_my_message', data=msg1)
    no64s1 = b64decode(r.text)
    r = requests.post('http://192.168.120.11:48407/sign_my_message', data=msg2)
    no64s2 = b64decode(r.text)
    with open("msg1.txt","rb") as f:
        sig1 = pickle.load(f)
        (r1, s1) = sig1.r,sig1.s
    with open("msg2.txt","rb") as f:
        sig2 = pickle.load(f)
        (r2, s2) = sig2.r,sig2.s
    print ("Message 1: ",msg1)
    print (f"Signature r={r1}, s={s2}")
    print ("\nMessage 2: ",msg2)
    print (f"Signature r={r2}, s={s2}")
    order = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    valinv = libnum.invmod( r1*(s1-s2),order)
    x1rec = ((s2*h1-s1*h2) * (valinv)) % order
    print (f"\nPrivate recovered !{x1rec}!")
    r = requests.post('http://192.168.120.11:48407/is_this_a_private_key', data=hex(x1rec))
    print(r.text)
except Exception as ex:
    print(ex)