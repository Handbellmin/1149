dp = [list(map(int,input().split())) for i in range(int(input()))]
for i in range(1,len(dp)):
  dp[i][0] = min(dp[i-1][1],dp[i-1][2])+dp[i][0]
  dp[i][1] = min(dp[i-1][0],dp[i-1][2])+dp[i][1]
  dp[i][2] = min(dp[i-1][0],dp[i-1][1])+dp[i][2]
print(min(dp[len(dp)-1]))
  


def s():
  n = int(input())
  table = [[0 for row in range(3)] for col in range(n)]
  
  for i in range(n):
    ls = input()
    for j in range(3):
      table[i][j] = int(ls.split(' ')[j])
  
  dp = [[0 for row in range(3)] for col in range(n)]
  dp[0][0],dp[0][1],dp[0][2] = table[0][0],table[0][1],table[0][2]
  
  for i in range(1,n):
    for state in range(3):
      if state == 0:
        dp[i][1] = dp[i-1][0] + table[i][1]
        dp[i][2] = dp[i-1][0] + table[i][2]
      elif state == 1:
        if dp[i][0] != 0:
          dp[i][0] = min(dp[i][0],dp[i-1][1] + table[i][0])
        else:
          dp[i][0] = dp[i-1][1] + table[i][0]
        if dp[i][2] != 0:
          dp[i][2] = min(dp[i][2],dp[i-1][1] + table[i][2])
        else:
          dp[i][2] = dp[i-1][1] + table[i][2]
      else:
        if dp[i][0] != 0:
          dp[i][0] = min(dp[i][0],dp[i-1][2] + table[i][0])
        else:
          dp[i][0] = dp[i-1][2] + table[i][0]
        if dp[i][1] != 0:
          dp[i][1] = min(dp[i][1],dp[i-1][2] + table[i][1])
        else:
          dp[i][1] = dp[i-1][2] + table[i][1]
  print (min(dp[n-1]))
  