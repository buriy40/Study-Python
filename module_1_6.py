my_dict = {'STM':2013 ,'Pirs':2011 ,'Oleg':1971 ,'Marina':2007}
print(my_dict)
print(my_dict.get('Oleg'))
my_dict.update({'Sergey':1999 ,
                'Kat':2020 ,
                'STM':2024})
print(my_dict)
print(my_dict.get('Katty', 'Нет такого абонента'))
print(my_dict.get('Pirs'))
#my_dict.pop('Sir')
#print(my_dict)
a = my_dict.pop('STM')
print(a)

my_set = {1, 2, 1, 5, 3, 5, 2, 'Z', 2, 'Z'}
print(my_set)
my_set.add(45)
my_set.add('A')
my_set.remove(1)
print(my_set)