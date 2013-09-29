# Make file for Lab Exercise 6 - Windows version
# WRITTEN BY: Michael Main (main@colorado.edu), Aug 11, 2004
#
# This makefile is used as follows to regenerate files for the sinewave program:
#   make intarray.o   --  Regenerates intarray.o by compiling
#   make sinewave.o   --  Regenerates sinewave.o by compiling
#   make sinewave.exe --  Regenerates the executable sinewave file by compiling
#   make              --  Same as "make sinewave.exe" (since sinewave.exe is 
#                     --  the 1st target)
#
# Two special targets may also be used with this makefile:
#   make all          --  Regenerates all files listed above
#   make clean        --  Erases all files listed above
#
# All compilations occur with -Wall and -gstabs.
# The clean command uses rm to remove all expendable files (rm is part of
# the cs1300 compiler tools from www.cs.colorado.edu/~main/cs1300/README.html).
EXPENDABLES = intarray.o sinewave.o sinewave.exe


sinewave.exe: intarray.o sinewave.o
	g++ -Wall -gstabs sinewave.o intarray.o -lm -o sinewave 

intarray.o: intarray.h intarray.cxx
	g++ -Wall -c -gstabs intarray.cxx

sinewave.o: intarray.h sinewave.cxx
	g++ -Wall -c -gstabs sinewave.cxx

clean:
	rm $(EXPENDABLES)

all:
	@make $(EXPENDABLES)


