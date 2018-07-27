name=input("enter your name : ")
age=input("enter your age : ")
phone=input("enter your num : ")


c=name+'\n'+age+'\n'+ phone

with open("m",mode="w")as f:
    f.write(c)

