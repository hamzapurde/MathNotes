notes={}
keys=[]
wController=0
print("Welcome")
while wController<1:
    answer=input("add student : 1\nsearch student : 2\n")
    if (answer=="1"):
        print("-----add student-----")
        studentN=input("Student Name : ")
        mathExam1=int(input("first math exam note : "))
        mathExam2=int(input("last math exam note : "))
        notes[studentN]={
            'first exam':mathExam1,
            'last exam':mathExam2,
            'average':(mathExam2+mathExam1)/2
            }
        keys.append(studentN)
        print(notes[studentN])
        c=input("wanna quit(1) or continue(2)\n")
        if(c=="1"):
            break
        elif(c=="2"):
            wController=0
        else:
            print("?")

    elif(answer=="2"):
        print("-----searh student-----")
        studentN=input("Student Name : ")
        print(notes[studentN])
        if(notes[studentN]['average']>=50):
            print("student passed math")
        elif(notes[studentN]['average']<=50):
            print("student failed from math")
        else:
            print("?")
        c=input("wanna quit(1) or continue(2)\n")
        if(c=="1"):
            break
        elif(c=="2"):
            wController=0
        else:
            print("?")
    else:
        print("?")

for student in notes:
    print(notes[student])
print("Thanks for Using Me :)")