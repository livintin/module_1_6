my_dict = {'Anton': 15111, 'Ivan': 15222, 'Kiril': 15333}
print(my_dict['Anton'])
my_dict['Andrey'] = 15444
print(my_dict['Andrey'])
my_dict.update({'Sergey': 15555,
                'Dmitry': 15666})
a = my_dict.pop('Anton')
print(a)
print(my_dict)

my_set = {1, 2, 3, 1, 2, 3, 'Anton', 'Sergey', 'Dmitry', 'Anton', 'Sergey', True}
print(my_set)
my_set.update({5, 'Igor'})
my_set.discard('Anton')
print(my_set)
