immutable_var = (1 ,2 ,True ,'Super')
print(immutable_var)
immutable_var[1] = 'z'
print(type(immutable_var))
print(immutable_var)

mutable_list = ['a ',1 ,'strings' ,True]
mutable_list[2] = 'z'
print (mutable_list)