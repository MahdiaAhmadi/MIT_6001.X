'''
module for problem set3 of MIT 6001.x 
author : Mahdia Ahmadi
date: 02/02/2025

'''


s = 'azcbobobegghakl'  # Example input

longest_substr = s[0]  # Start with the first character
current_substr = s[0]  # Track the current alphabetical substring

for i in range(1, len(s)):  # Start from the second character
    if s[i] >= s[i - 1]:  # Check if characters are in alphabetical order
        current_substr += s[i]  # Add to current substring
    else:
        if len(current_substr) > len(longest_substr):  # Update longest if needed
            longest_substr = current_substr
        current_substr = s[i]  # Start a new substring

# Final check in case the longest substring is at the end
if len(current_substr) > len(longest_substr):
    longest_substr = current_substr

print(f'Longest substring in alphabetical order is: {longest_substr}')



