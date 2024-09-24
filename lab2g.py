#!/usr/bin/env python3

#Author: Mohamed Farah
#Author ID: mfarah19
#Date Created: 2024/09/23

import sys

#issue solution: timer can be defined anytime before the first time it is called
#defining it twice bricks the program

#timer = int(sys.argv[1])

if len(sys.argv) <= 1:
	timer = 3
else:
	timer = int(sys.argv[1])

while timer >= 1:
	print (timer)
	timer = timer - 1
print ('blast off!')
