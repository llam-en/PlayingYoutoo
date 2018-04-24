#!/usr/bin/env python3
import os
import sys
import time
import requests
import datetime



def Usage():
  exit("usage: {}  <search term for youtube here>".format(sys.argv[0]))



PROXIES = {
  "http":"socks5h://127.0.0.1:9050",
  "https":"socks5h://127.0.0.1:9050",
}



if len(sys.argv) > 1:
  pass
else:
  Usage()



search_term = str(sys.argv[1]).replace(" ", "+")



if len(sys.argv[1]) > 0:
  url = "https://www.youtube.com/results?search_query={}".format(search_term)
else:
  Usage()



r = requests.get(url, proxies=PROXIES)




### Messy replacement and splitlines section. <_<
seek_var = r.text.replace("\"", "\n\"\n")

seek_var = seek_var.replace("\"", "\n\"\n")
seek_var = seek_var.replace("<", "\n<\n")
seek_var = seek_var.replace(">", "\n>\n")

seek_var = seek_var.replace("comhttp", "com\nhttp")
seek_var = seek_var.replace("http", "\nhttp")

seek_var = seek_var.splitlines()






current_time = str(datetime.date.today())
current_time = current_time.replace("-", "") + "-"
current_time = str(current_time) + str(datetime.datetime.now().hour)
current_time = str(current_time) + str(datetime.datetime.now().minute)



save_file = "{}_{}.out".format(search_term.replace("+", "-"), current_time)
count = 0
prev_item = ""



for item in seek_var:
  #    v----    '&amp;' fix here
  if "&amp;" in item:
    item = item.replace("&amp;", "/n&amp;\n")
    item = item.splitlines()


  ## 'count', is a part of checking for a match with the previous 'item'
  ##    It checks if this is the first iteration or not.
  if "/watch?v=" in item:
    if count == 0:
      with open(save_file, "a") as f:
        if not item.startswith("http"):
          f.write("https://www.youtube.com{}\n".format(item))
        elif item.startswith("http"):
          f.write("{}\n".format(item))
    if count == 1:
      if item == prev_item:
        pass
      else:
        with open(save_file, "a") as f:
          if not item.startswith("http"):
            f.write("https://www.youtube.com{}\n".format(item))
          elif item.startswith("http"):
            f.write("{}\n".format(item))

        prev_item = item  # <-- set prev_item, after writing it, here!


  if count == 0:
    count = 1



print("File Edited: {}".format(save_file))



# o/ <3
