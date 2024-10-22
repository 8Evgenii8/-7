my_dict = {'Paha': 1999, 'Cveta': 1994, 'Danis': 2020 }
print(my_dict)
print(my_dict['Paha'])
print(my_dict.get('Kat'))
my_dict.update({'Pavel': 2018, 'Anton': 2012})
del my_dict ['Cveta']
print(my_dict)

my_set = {1,"яблоко", 42.123,}
print(set(my_set))
print(my_set.add(6,))
print(my_set.add(7))
print(my_set.discard(1))
print(my_set)