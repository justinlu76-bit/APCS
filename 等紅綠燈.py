#https://zerojudge.tw/ShowProblem?problemid=q181

a,b = map(int,input().split())
n = int(input())
z = a + b
t = list(map(int,input().split()))
total = 0
for i in range(n):
  m = t[i]%z
  if m > a:
    h = b-(m-a)
  elif m < a:
    h = 0
  else:
    h = b
  total += h
print(total)
