import webbrowser
import time
import os
# from array import *
#url = "http://www.bing.com/news?q=Northeast+US+News&FORM=NSBABR"
#webbrowser.open(url,new=0,autoraise=True)
#time.sleep(4)
#browserExe = "firefox.exe"
#os.system("taskkill /f /im "+browserExe)

# print("before calling close")
# webbrowser.close()
#print("after calling close")
#url = "http://www.bing.com/news?q=South+US+News"
#webbrowser.open_new_tab(url)
url = ["http://www.bing.com/news?q=Northeast+US+News&FORM=NSBABR","http://www.bing.com/news?q=South+US+News&FORM=NSBABR","http://www.bing.com/news?q=Midwest+US+News&FORM=NSBABR",
"http://www.bing.com/news?q=West+US+News&FORM=NSBABR","http://www.bing.com/news?q=Africa+News&FORM=NSBABR","http://www.bing.com/news?q=Americas+News&FORM=NSBABR",
"http://www.bing.com/news?q=Asia+Pacific+News&FORM=NSBABR","http://www.bing.com/news?q=Europe+News&FORM=NSBABR","http://www.bing.com/news?q=Middle+East+News&FORM=NSBABR",
"http://www.bing.com/news?q=Movie+%26+TV+News&FORM=NSBABR","http://www.bing.com/news?q=Music+News&FORM=NSBABR",
"http://www.bing.com/news?q=Technology+News&FORM=NSBABR",
"http://www.bing.com/news?q=Science+News&FORM=NSBABR","http://www.bing.com/news?q=business+news&FORM=NSBABR","http://www.bing.com/news?q=political+news&FORM=NSBABR",
"http://www.bing.com/news?q=NFL+News&FORM=NSBABR","http://www.bing.com/news?q=MLB+News&FORM=NSBABR","http://www.bing.com/news?q=NBA+News&FORM=NSBABR",
"http://www.bing.com/news?q=NHL+News&FORM=NSBABR","http://www.bing.com/news?q=Soccer+News&FORM=NSBABR","http://www.bing.com/news?q=CBB+News&FORM=NSBABR",
"http://www.bing.com/news?q=Golf+News&FORM=NSBABR","http://www.bing.com/news?q=Tennis+News&FORM=NSBABR","http://www.bing.com/news?q=health+news&FORM=NSBABR",
"http://www.bing.com/news?q=products+news&FORM=NSBABR","http://www.bing.com/news?q=CFB+News&FORM=NSBABR","http://www.bing.com/news?q=Northeast+US+News&FORM=NSBABR",
"http://www.bing.com/news?q=Northeast+US+News&FORM=NSBABR","http://www.bing.com/news?q=Music+News&FORM=NSBABR","http://www.bing.com/news?q=Technology+News&FORM=NSBABR"]
for u in url:
 webbrowser.open(u,new=0,autoraise=True)
 time.sleep(4)
 
browserExe = "firefox.exe"
os.system("taskkill /f /im "+browserExe)
 

 #time.sleep(10)
#webbrowser.close(url)
  #print(u)

# webbrowser.open_new_tab(url)
