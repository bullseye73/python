# https://datascienceschool.net/view-notebook/465066ac92ef4da3b0aba32f76d9750a/

import datetime
dt = datetime.datetime.now()
print(dt) # $ 2019-03-03 09:44:39.401773

#dt = datetime.datetime.strptime(str(datetime.datetime.now()), "%Y-%m-%d %H:%M")
dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(dt) # $ 2019-03-03 09:44:39


