#include <iostream>
using namespace std;

// Base class
class Shape 
{
public:
  virtual void setWidth(int) =0;
  virtual void setHeight(int) =0;
  virtual int getWidth() const =0;
  virtual int getHeight() const =0;
  void throwError() const;
  virtual void virtualThrowError() const;
  protected:
  int width;
  int height;
};

void Shape::throwError() const {
	throw "foo";
}
void Shape::virtualThrowError() const {
	throw "bar";
}

// Derived class
class Rectangle: public Shape
{
public:
  virtual void setWidth(int w);
  virtual void setHeight(int h);
  virtual int getWidth() const;
  virtual int getHeight() const;
  void throwError() const;
  virtual void virtualThrowError() const;
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

void Rectangle::throwError() const {
	cerr << "no I don't wanna throw a foo." << endl;
}

void Rectangle::virtualThrowError() const {
	cerr << "no I don't wanna throw a bar." << endl;
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

  Rect.throwError();
  Rect.virtualThrowError();

  printDimensions(Rect);

  cout << "Total area = " << Rect.getArea() << endl;

  Shape *Rect2 = new Rectangle();
  Rect2->setWidth(15);
  Rect2->setHeight(10);
  printDimensions(*Rect2);

  Rect2->virtualThrowError();
  Rect2->throwError();
}

