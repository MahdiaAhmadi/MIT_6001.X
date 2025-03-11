'''
module for problem set 2 of MIT 6001.x 
author : Mahdia Ahmadi
date: 02/02/2025
'''


s = 'azcbobobegghakl'
count_bob = 0
name = 'bob'

for i in range(len(s) - 2):  # Iterate up to len(s) - 2 to avoid index out of range
    if s[i:i+3] == name:  # Check if substring matches 'bob'
        count_bob += 1

print(f'Number of times bob occurs is: {count_bob}')

