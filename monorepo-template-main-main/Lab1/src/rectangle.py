"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""

class Shape:
    def __init__(self, width, height):
        self._width = width  # Making width and height private
        self._height = height

    # Getter for width
    def get_width(self):
        return self._width

    # Getter for height
    def get_height(self):
        return self._height

    # Setter for width
    def set_width(self, width):
        self._width = width

    # Setter for height
    def set_height(self, height):
        self._height = height

    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return self.get_width() * self.get_height()

if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle(3, 4)

    # Print out the area
    print("area:", rect.area())
