# Set Data Type: Set is collection of element having different data types
# --> For the set we use '{}' brackets
# --> It is not get accept dubblicate value
# --> indexing not posible
# --> slicing is not possible
# --> It is Mutable naturaly
# --> it is print randomly value

# Example of not get dubblicate value:

s = {10,'razin',25.5,True,3j,10}
print(s)
# o/p:- {True, 'razin', 3j, 10, 25.5}
'''
# Example of indexing is not possible:
print(s[1]) # show an error (Type Error)

# Example of slicing is not possible:
print(s[1:4]) # show an error (Type Error)
'''
s.add(200)
print(s)
# o/p:{'razin', True, 200, 3j, 10, 25.5}


s.remove('razin')
print(s)
#o/p:{True, 200, 3j, 10, 25.5}


