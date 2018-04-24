#!/usr/bin/env python3
import os
import sys
import time


readme = sys.argv[1]


with open(readme, "r") as f:
  url_list = f.read().splitlines()

  for url in url_list:
    if url.startswith("https://www.youtube.com/watch?v="):
      os.system("torsocks  mpv  --no-video  \
        --ytdl-format=best  {}".format(url))

      time.sleep(0.2)



# o/ <3
