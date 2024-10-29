#furniture = ['table' , 'chair' , 'wardroube']
#print(furniture)
#furniture[1] = 'sofa'
#print(furniture)
#furniture.append('Oleg')
#print(furniture)
#furniture.extend('Marina')
#print(furniture)
#furniture.remove('sofa')
#print(furniture)
from lib2to3.fixes.fix_tuple_params import tuple_name

tuple_ = 1, 2, 3, 4
tuple_2 = (1, 2, 3, 4)
tuple_3 = tuple([1, 2, 3,4])
print(type(tuple_))
print(tuple_2)
print(tuple_3)