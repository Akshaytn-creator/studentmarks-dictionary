n = int(input("Enter number of students: ")) 
 
res = {} 
 
for i in range(n): 
    print("Enter Details of student Number:", i+1) 
 
    rno =(input("enter Roll No: ")) 
    name = (input("enter Name: "))
    marks = int(input("enter Marks: ")) 
 
    res[rno] = [name, marks] 
 
print(res)
 
for student in res: 
    if res[student][1] > 75: 
        print(res[student][0]) 
        print("congrats")