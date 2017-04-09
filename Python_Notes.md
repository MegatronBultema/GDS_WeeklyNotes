write clean code, employers will look at your github



Dynamic typing - Python will try to interpret what datatype a variable should be at runtime.
Duck typing - if it looks like a duck and sounds like a duck, it is used as a duck
Differences betwee python 2 and 3 : print(), xrange -> range
    can use: from __future__ import absolute_import, division, print_function
    or: from builtins import *
    to write a py2/3 compatable code

• Mutable - Refers to a data structure whose state can be altered after it has been created
• Immutability - Refers to a data structure whose state cannot
be modified after it has been created

Lists vs Sets:
  Use sets whenever you will be checking membership

Dictionaries
  Use 'Indiana' in my_dict and NOT 'Indiana' in my_dict.keys() ('Indiana' in my_dict uses hash map)

Generators
  Allow us to build up an iterator that evaluates lazily (only loads values into memory when explicitly needed to perform some calculation/operation)

Pep8 - The Style Guide for Python Code

Debugger:
pdb.set_trace()
  Learn how to use a debugger. It will save you a lot of pain. . .
  h help
  b set a break-point
  where show call stack
  s execute next line, stepping into functions n execute next line, step over functions
  c continue execution
  u move up one stack frame
  d move down one stack frame

Tips:
  • General for loops to iterate over lists (instead of indexing in)
  • Using enumerate if we need to use the index
  • Using with statements when working with files
  • Using izip to iterate over two lists at the same time
  • Using a set to check membership
  • list (and other) comprehensions
  • squares = [x**2 for x in xrange(1000)]
  • (if x:) instead of (if x == True:) or
  (if x is not None:)
  • Leveraging numpy and pandas (when we get there)
