#!/usr/bin/env python

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2013-04-05 13:54:50 (jonah)>

# This is a simple class to time things. 
import time 

class Timer():
   def __enter__(self):
       self.start = time.time()
   def __exit__(self, *args):
       print(time.time() - self.start)
