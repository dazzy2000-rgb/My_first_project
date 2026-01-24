from Python_trenning.utils import utils_jb61

user_1={
    'first_name':'John',
    'last_name':'Doe',
    'email':'abc@abc.co',
    'age':22,
}
user_2={
    'first_name':'Mark',
    'last_name':'Doelko',
    'email':'bbc@ccvco',
    'age':16,
}
utils = utils_jb61()
age_1=utils.age_calculator(user_1['age'])
age_2=utils.age_calculator(user_2['age'],20)
print(f'{age_1} and {age_2}')
if utils.email_validator(user_1['email']):
    print(f'{user_1["email"]} is valid')
if utils.email_validator(user_2['email']):
    print(f'{user_2["email"]} is valid')

