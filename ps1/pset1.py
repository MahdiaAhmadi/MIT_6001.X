'''
module test for MIT 6001.x course
author: Mahdia Ahmadi

date: 01/02/2025

'''


s = input('enter your desired string: \n')
count_vovel= 0
vovel_list = ['a','e','i','o','u']

for char in s:
    if char in vovel_list:
        count_vovel+=1

if count_vovel > 0:
    print(count_vovel)
else:
    print('Not Vovel is included in the string')



