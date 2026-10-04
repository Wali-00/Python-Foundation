""" H. Good or Bad
Given a string S. Determine whether this string is Good or Bad.

Note: The string is Good if and only if it has "010" or "101" as one of its sub-strings and it's not necessary to have both of them.

A substring of a string is a contiguous subsequence of that string. So, string "forces" is substring of string "codeforces", but string "coder" is not.
It's guaranteed that S contains only '1s' and '0s'.
Output
For each test case, print "Good" if the string is Good otherwise, print "Bad"""




T = int(input())
for i in range(T):
    s = input()
    a=(s.find("010"))
    b=(s.find("101"))
    if a!=-1 or b!=-1:
        print("Good")
    else:
        print("Bad")   
 