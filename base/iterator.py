
gen = (x for x in range(10))
for x in range(10):
    print(gen.__next__())

dictionary = {
    'a': 'A',
    'b': 'B',
    100: ['tr', 45, {'bg': 56}],
    'erw': {'bird': 'duck', 'animal': 'cat'},
    3: 2908,
    'field_for_delete': 654
}

it_dict = iter(dictionary)
print(next(it_dict))
print(next(it_dict))
print(next(it_dict))
print(next(it_dict))
print(next(it_dict))

