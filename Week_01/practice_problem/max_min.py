# M. Replace MinMax
# Given a number N and an array A of N numbers. Print the array after doing the following operations:

# Find minimum number in these numbers.
# Find maximum number in these numbers.
# Swap minimum number with maximum number.
# Input

# It's guaranteed that all numbers are distinct.

# Output
# Print the array after the replacement operation.


N = int(input())
lis = list(map(int, input().split()))


mi_index = lis.index(min(lis))
ma_index = lis.index(max(lis))
lis[mi_index], lis[ma_index] = lis[ma_index], lis[mi_index]

print(*lis)