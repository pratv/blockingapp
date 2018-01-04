import time
from datetime import datetime as dt
host_temp="hosts"
host_path=r'C:\Windows\System32\drivers\etc'
redirect="127.0.0.1"
website_list=["www.facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,22)<dt.now():
     print('workinghours')
     with open(host_path,'r+') as file:
           content=file.read()
           print(content)
           for item in website_list:
                 if item in content:
                       pass
                 else:
                        file.write(redirect+" "+item+"\n")
    else:
         with open(host_path,'r+') as file:
           content=file.readlines()
           print(content)
           for line in content:
               if not any(item in line for item in website_list):
                   file.write(line)
    time.sleep(5)
