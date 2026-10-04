"""Given a number N and an array A of N numbers. Print the lowest number and its position.

Note: if there are more than one answer print first one's position.

Input
First line contains a number N (2≤N≤1000) number of elements.

Second line contains N numbers (-105 ≤ Ai ≤ 105).

Output
Print the lowest number and its position (1-index) """

N = int(input())
lis = list(map(int, input().split()))


m = min(lis)
fin = lis.index(m)
print(m,(fin+1))