#!/usr/bin/env python2

# n_hellos = 1
target_hellos = 5

"""
while n_hellos <= target_hellos:
    print "This is my "+str(n_hellos)+"th hello!"
    n_hellos = n_hellos + 1
"""

for i in range(1,target_hellos+1):
    if i == 1:
        print "This is my 1st hello"
    if i == 2:
        print "This is my 2nd hello"
    if i == 3:
        print "This is my 3rd hello"
    if i > 3:
        print "This is my "+str(i)+"th hello"
