nums = input().split()
if len(nums) == len(set(nums)):
    print('Все числа разные')
elif len(set(nums)) == 1:
    print('Все числа равны')
else:
    print('Есть равные и неравные числа')
