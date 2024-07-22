grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
bal={}
students1=list(students)
print(students1)
students1.sort()
print(students1)
bal.update({students1[0]:sum(grades[0])/len(grades[0]),students1[1]:sum(grades[1])/len(grades[1])})
bal.update({students1[2]:sum(grades[2])/len(grades[2]),students1[3]:sum(grades[3])/len(grades[3])})
bal.update({students1[-1]:sum(grades[-1])/len(grades[-1])})
print('Средний балл-',bal)


