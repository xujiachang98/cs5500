# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	MObject is a concrete class. It is not an abstract class because it does not contain any abstract methods.
	Its __init__ method is defined without any abstract or unimplemented methods.

1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	The commented-out __del__ method is a destructor method. It is used when an object is about to be destroyed or garbage collected. It can be used to perform cleanup operations or release resources associated with the object removing from memory.

1. What class does Texture inherit from?
	Image class. In Python, we can specify inheritance by placing the name of the parent class in parentheses when defining a new class. 

1. What methods and attributes does the Texture class inherit from 'Image'? 
	It inherits all the methods and attributes from the Image class because it's a subclass of Image. 
	
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	It depends. If it is an "is-a" relationship, suggesting that a Texture "is-a" kind of Image. If is is an 'has-a' relationship, a Texture is not fundamentally a type of Image but uses an Image as part of its functionality. Then we can refactor the code: 
	class Texture:
    def __init__(self, w, h):
        self.image = Image(w, h)

1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	Yes, Python automatically creates a default constructor for you. This default constructor takes no arguments and does not perform any specific initialization. 

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?
	No, they are not. It may lead to race conditions and without proper synchronization, concurrent access can lead to issues. Although Python's GIL can help mitigate some concurrency issues, it does not guarantee the thread safety of a singleton implementation. 

*edit the code directly*  
  
