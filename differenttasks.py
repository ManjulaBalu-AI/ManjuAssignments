class multiplefunctions():
    def subfields():
        print("Subfields in AI are:")
        print("Mechine learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Naural Language Processing")
    def oddeven():
        num=int(input("Enter the num:"))   
        remin=(num%2)
        if(remin==1):
            print(num, "is odd")
        else:
            print(num, "is even")
    def elegible():
        gen=str(input("your gender:"))
        age=int(input("your age:"))
        if(gen=="male"):
            if age>21:
                print("Elegible")
            else:
                print("Not elegible")
        else:   
            if age>18:
                print("Elegible")
            else:
                print("Not elegible")
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        tot=(sub1+sub2+sub3+sub4+sub5)
        print("total=",tot)
        perc=float(tot/5)
        print("percentage=",perc)
    def triangle():
        ht=int(input("Height:"))
        bt=int(input("Breath:"))
        print("Area formula=(Height*Breath)/2")
        ar=(ht*bt)/2
        print("Area of Triangle:",ar)
        ht1=int(input("Height1:"))
        ht2=int(input("Height2:"))
        bt1=int(input("Breath1:"))
        print("Perimeter formula= Height1+Height2+Breath")
        pr=(ht1+ht2+bt1)
        print("Perimeter of Triangle:",pr)
    def agecategory():
        age=int(input("Enter the age:"))
        if (age<18):
            print("Child")
        elif(age<35):
            print("adult")
        elif(age<58):
            print("ciizen")
        else:
            print("senior citizen")
    def positiveornegative():
        num=int(input("enter any number:"))
        if num>0:
            print("No is positive")
        elif num<0:
            print("No is negative")
        else:
            print("No is zero")
    def divisablebyfive():
        numb=int(input("enter the number to check:"))
        remind=(numb%5)
        if remind==0:
            print("number is divisable by 5")
        else:
             print("number is  not divisable by 5")