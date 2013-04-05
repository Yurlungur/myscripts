#!/usr/bin/env python3

def make_x_to_the_n(x):
    def x_to_the_n(n):
        return x**n
    return x_to_the_n

def main():
    three_to_the_n=make_x_to_the_n(3)
    print(three_to_the_n(2)) # Should print 9.
    return

if __name__ == "__main__":
    main()
          
