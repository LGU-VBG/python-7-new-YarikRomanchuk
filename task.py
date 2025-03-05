def merge_lists_to_dict(keys, values):
    return dict(zip(keys, values))

result1 = merge_lists_to_dict(keys=['name', 'age', 'city'], values= ['Yaroslav', 16, 'Vyborg'])
print(result1)

result2 = merge_lists_to_dict(['name', 'age'], values=['Ivan', 18])
print(result2)
