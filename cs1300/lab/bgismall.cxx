// FILE: bgismall.cpp
// Written by: Michael Main (main@colorado.edu) -- Sep 11, 1998
// A small demonstration program using Borland's BGI.

#include <graphics.h> // Provides the BGI graphics functions

// Call this function to draw an isosoles triangle with the given base and
// height. The triangle will be drawn just above the botton of the screen.
void triangle(int base, int height)
{
    int maxx = getmaxx( );
    int maxy = getmaxy( );

    line(maxx/2 - base/2, maxy - 10, maxx/2 + base/2, maxy - 10);
    line(maxx/2 - base/2, maxy - 10, maxx/2, maxy - 10 - height);
    line(maxx/2 + base/2, maxy - 10, maxx/2, maxy - 10 - height); 
}

int main(void)
{
    int maxx, maxy;  // Maximum x and y pixel coordinates
    int i;           // Loop control variable

    // Put the machine into graphics mode and get the maximum coordinates:
    initwindow(450, 300);         
    maxx = getmaxx( );
    maxy = getmaxy( );

    // Draw a yellow pixel in the center of the screen:
    putpixel(maxx/2, maxy/2, YELLOW);
    
    // Draw a white circle with a radius of 50 pixels:
    setcolor(WHITE);    
    circle(maxx/2, maxy/2, 50);
    
    // Draw a bunch of blue triangles:
    setcolor(LIGHTBLUE);
    for (i = 2; i <= 100; i++)
        triangle(maxx/i, maxy/i);
    
    // Print a message and ait for a key to be pressed:
    outtextxy(20, 20, "Please press <return> to finish.");    
    getch( );
    
    // Switch back to text mode:
    closegraph( );
}

