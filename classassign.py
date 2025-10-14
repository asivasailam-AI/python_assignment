class functions():

    def subfields():
        AIfields = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        print("Sub-fields in AI are:")
        for i in AIfields:
            print(i)
    subfields()


    def OddEven():
        number = int(input("Enter a number: "))
        if(number%2==0):
            print(f"{number} is a even number")
        else:
            print(f"{number}is a odd number")
    OddEven()


    def eligiblityformarriage():
        gender = input("enter your gender")
        age = int(input("enter your age"))
        if (gender == "male" and age >= 21):
            print("elgible")
        elif(gender == "female" and age >= 18):
            print("eligible")
        else:
            print("not elgible")
    eligiblityformarriage()



    def findpercentage():
        subject1 = float(input("Enter 1st subject mark"))
        subject2 = float(input("Enter 2nd subject mark"))
        subject3 = float(input("Enter 3rd subject mark"))
        subject4 = float(input("Enter 4th subject mark"))
        subject5 = float(input("Enter 5th subject mark"))
        total = subject1 + subject2 + subject3 + subject4 + subject5
        print("total",total)
        percentage = total/500 * 100
        print("percentage",percentage)
    findpercentage()




    def triangle():
        height = float(input("height of triangle"))
        breadth = float(input("breadth of triangle"))
        print("Area of triangle: height*breadth/2")
        area = (height * breadth)/2
        print("Area of triangle",area)

        height1 = float(input("height1 of triangle"))
        height2 = float(input("height2 of triangle"))
        breadth = float(input("breadth of triangle"))
        print("perimeter of triangle: height1+height2+breadth")
        perimeter = height1 + height2 + breadth
        print("perimeter of triangle", perimeter)
    triangle()
   







