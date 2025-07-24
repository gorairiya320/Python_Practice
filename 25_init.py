class Stu:
    name="Riya"
    def __init__(self):
        print("I am a constructor!")
s1=Stu()


class Stu2:
    def __init__(self,fullname):
        self.name=fullname
        print("I am a constructor!")

stu=Stu2("Riya")
print(stu.name)

stu2=Stu2("Piya")
print(stu2.name)