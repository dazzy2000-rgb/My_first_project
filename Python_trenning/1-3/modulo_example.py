
summery_1=0
summery_2=0
nums=[11,15,24,8,13]
for num in nums:
    if num % 2 == 0:
        summery_1=summery_1+num
        print(f'{num} this num is zugi')

    else:
        print(f'{num} this num is not zugi')
        summery_2 = summery_2 + num
print(f'{summery_2} its sum are nums  are not zugi')
print(f'{summery_1} its sum are nums zugi')