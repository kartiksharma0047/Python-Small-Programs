# 5. Longest Palindromic Substring :- Given a String s, return the longest palindromic substring in s.
# Example - 
# s="babad"
# output="bab"
# Note- aba is also correct answer. But return the first palindromic substring

s="acad"
final_Output=""
for i in range(0,len(s)):
    temp=s[i]
    for j in range(i+1,len(s)):
        temp+=s[j]
        if len(temp)>1:
            reversed_str=temp[::-1]
        if reversed_str==temp and len(temp)>len(final_Output):
            final_Output=temp
if len(final_Output)==0:
    final_Output=s[0]
print(final_Output)