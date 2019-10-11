def stockBuySell(A,n):
  if A == sorted(A):
    print ("(" + str(0) + " " + str(n-1) + ")",end=" ")
  elif A == sorted(A,reverse=True):
    print ("No Profit",end = " ")
  else:
    local_min = []
    local_max = []
  for i,v in enumerate(A):
    if i == 0:
      if v < A[i+1]:
        local_min.append(i)
      elif i == n-1:
        if v > A[i-1]:
          local_max.append(i)
      else:
        if A[i-1] <= v and v >= A[i+1]:
          local_max.append(i)
        if A[i-1] >= v and v <= A[i+1]:
          local_min.append(i)
        if len(local_max) == len(local_min):
          for i in range(len(local_max)):
            x = " ".join([str(local_min[i]),str(local_max[i])])
            print ("("+x+")",end=" ")
        else:
            x = " ".join([str(max(local_min)),str(max(local_max))])
            print ("("+x+")",end = " ")
