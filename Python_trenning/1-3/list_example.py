

student_names=['maxim','alex']
grades=[12,31]
cities=['lod','london','Rome']
cities.append('Madrid')
cities.insert(1,'rome')
cities.remove('Madrid')
cities[2:4]

for name in student_names:
    print(name)
l=len(name)
print(f'the len of {name} is {l}')

city_index_1=[1]
length_of_list=len(cities)
lod_counter=cities.count('lod')
is_rome='Rome' in cities
is_madrid='Madrid' in cities

print (f"is_madrid is {is_madrid}")
print (f"is_rome is {is_rome}")