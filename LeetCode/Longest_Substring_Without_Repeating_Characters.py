# #2. Longest Substring Without Repeating Characters :- 
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

s = "abcabcbb"
max_len=0
for val in range(len(s)):
    temp=""
    for j in range(val,len(s)):
        if s[j] not in temp:
            temp+=s[j]
        else:
            break
    max_len=max(max_len,len(temp))
print(max_len)