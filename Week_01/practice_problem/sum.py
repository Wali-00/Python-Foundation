"""Given a number N and an array A of N digits (not separated by space). Print the summation of these digits.

Input
First line contains a number N

Second line contains N digits 

Output
Print the summation of these digits."""

N = int(input())
lis = list(input())
sum=0

for i in range(0,N):
    sum+=int(lis[i])
print(sum)