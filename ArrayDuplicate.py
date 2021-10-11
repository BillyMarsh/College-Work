import array as arr

a = arr.array('i', [2, 3, 4, 2])

# Get Duplicated

t = 0
for i in range(0, len(a)):    
  for j in range(i+1, len(a)):    
    if(a[i] == a[j]):    
      print(a[j]);
      t = t + 1
print("Number of Duplicates: ", t)

