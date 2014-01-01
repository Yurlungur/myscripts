#include <iostream>
#include <cassert>
using namespace std;

// Base class
class Shape 
{
public:
  virtual void setWidth(int) =0;
  virtual void setHeight(int) =0;
  virtual int getWidth() const =0;
  virtual int getHeight() const =0;
protected:
  Shape() {};
  int width;
  int height;
};

// Derived class
class Rectangle: public Shape
{
public:
  Rectangle() { cout << "I constructed a rectangle!" << endl; }
  void setWidth(int w);
  void setHeight(int h);
  int getWidth() const;
  int getHeight() const;
  int getArea()
  { 
    return (width * height); 
  }
};

void Rectangle::setWidth(int w)
{
  width = w;
}
void Rectangle::setHeight(int h)
{
  height = h;
}
int Rectangle::getWidth() const {
  return width;
}
int Rectangle::getHeight() const {
  return height;
}

void printDimensions(const Shape& s) {
  cout << "Width = " << s.getWidth() << "\n"
       << "Height = " << s.getHeight()
       << endl;
}

int main(void) {
  Rectangle Rect;
  Rect.setWidth(5);
  Rect.setHeight(7);

  printDimensions(Rect);

  cout << "Total area = " << Rect.getArea() << endl;
}
