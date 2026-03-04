def leng(x):
  counter = 0
  for i in x:
    counter+=1
  return counter


def find(wrd,x):
  leng = len(wrd)
  for i in range(leng):
    if wrd[i] == x:
      return i
  return -1



def insert(lst,id,item):
  result =[]
  if id < 0:
    id = len(lst)+id
  if id < 0:
    id = 0
  elif id > len(lst):
    id = len(lst)
  result[:] = lst[:id] + [item] + lst[id:]
  return result

def ranje(sta,end,):
  result =[]
  current = sta
  while current<end:
    result.append(current)
    current+=1
  return result
  
