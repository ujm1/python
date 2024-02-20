A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A:
    total+=score
average=total/len(A) #79.0. A의 length(개수인듯)
print(average)
print(total) #790