# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Yes, the names of the member functions correlate to what they do. They are good 'verbs' where the name of the function describes the action the code is doing. For example in List: append(item) indicates that the method appends an item to the end of the list. remove(item) indicates that the method removes the first occurrence of the specified item from the list.
In dictionary: append(item) indicates that the method appends an item to the end of the list. remove(item) indicates that the method removes the first occurrence of the specified item from the list.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

Lists are ordered and indexed by integers and allow duplicates, while dictionaries use keys for unique and efficient access to values. Lists are ordered collections implemented as dynamic arrays. Dictionaries are key-value stores implemented as hash tables. 

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, lists in Python allow for random access.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

Pros: 
1. They can handle various types of data, which is especially useful in dynamic and heterogeneous programming environments.
2. Easy to use

Cons:
1. Type errors may happen, it is hard to debug
2. It takes time to check types so it may cause performace overhead
3. Take time to maintenance

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

Yes, the functions and methods in the Requests module are well-named and follow clear naming conventions.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

I see that there are some member functions, especially in the lower-level classes, that can include a relatively large number of arguments. For example, the requests.request() function, which is a lower-level method for sending HTTP requests, allows for various optional keyword arguments, including methods, urls, params, data, json, headers, cookies, files, auth, and so on.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

 **kwargs is a special syntax that allows a function or method to accept an arbitrary number of keyword arguments as input. Often used when a function or method needs to handle additional, unspecified arguments beyond those explicitly defined in its parameter list.

 It is good for its flexibility and extensibility.

 It is bad because it lowers readability and it may cause type errors.


4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

Set arguments to None or predetermined values depends on the desired behavior of the method and the level of customization and clarity you want to provide to users of the method. 

Arguments can be set to anything besides `None`

Predetermined values can make the method's behavior more explicit and can serve as starting points for customization.

