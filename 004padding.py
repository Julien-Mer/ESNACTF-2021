from base64 import b64decode,b64encode
import requests, sys
from paddown import Paddown

if __name__ == "__main__":
    port = 51339
    sessid = {"PHPSESSID": "8bueghs9j12moinnajk297apgb"}
    
    S = requests.Session()
    res = S.get(f"http://192.168.120.11:{port}/get_santa_message", cookies=sessid).text
    print(res)
    ciphertext=b64decode(res)

    class MyPaddown(Paddown):
        i=1
        # Implement has_valid_padding to check for padding errors, return False on everything but valid padding.
        def has_valid_padding(self, cipher):
            r = S.post(f"http://192.168.120.11:{port}/check_santa_message_correct", data=b64encode(cipher), cookies=sessid)
            res=r.text
            if "not happy" in res:
                return False
            if "correct" in res:
                print(f"Correct {self.i}")
                self.i=self.i+1
                return True

    plaintext_decrypted = MyPaddown(ciphertext).decrypt()
    print(plaintext_decrypted)