class Stuent:
    def __init__(self,name):
        self.name=name

    def avg(self,m1,m2,m3):
        self.math=m1
        self.english=m2
        self.science=m3

        avg=(m1+m2+m3)/3
        print(avg)


s=Stuent("Riya")
print(s.name)
s.avg(20,10,30)