#
# person_1
# first_name_1='margarita'
# last_name_1='dobrynin'
# age_1=45
# number_of_legs_1=4
# address_1='lod'

# person_2
# first_name_2='max'
# last_name_2='green'
# age_2=41
# number_of_legs_2=4
# address_2='lod'
person_1={
    'first_name_1':'Margarita',
    'last_name_1':'Dobrynin',
    'age_1':45,
}
person_2={
    'first_name_2':'Max',
    'last_name_2':'green',
    'age_2':41,
}
if person_1['age_1']>person_2['age_2']:
    print(person_2['first_name_2'])
    print(person_2['last_name_2'])
    print(person_2['age_2'])
    print(person_1['first_name_1'])
    print(person_1['last_name_1'])
    print(person_1['age_1'])
else:
    print(person_1['first_name_1'])
    print(person_1['last_name_1'])
    print(person_1['age_1'])
    print(person_2['first_name_2'])
    print(person_2['last_name_2'])
    print(person_2['age_2'])