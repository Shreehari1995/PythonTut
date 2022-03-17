# import file
# print(file.a,file.b)
#######################################

# from file import a, b
# print(a,b)
#######################################

# from pack1 import file2
# from file2 import x,y
# print(x, y)

# from pack1.file2 import x , y
# print(x,y)

#########################################

# from file import display as d
# d()
# def display():
#     print("hello")
#
# display()
# d()

##########################################
from file import *

print(a,b)
display()

###########################################
from pack1.pack2.file3 import a,b
print(a,b)

###########################################


