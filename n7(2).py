
mix_list  = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
how_many = {}
for item in mix_list:
    if item in how_many:
        how_many[item] += 1
    else:
        how_many[item] = 1
    if how_many[item] >=2:
        mix_list.remove(item)
print(mix_list)
    