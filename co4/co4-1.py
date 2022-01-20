class Rectangle:
    def __init__(self):
        self.l=int(input("enter the length"))
        self.b=int(input("enter the breadth"))
        self.area=self.l*self.b
        self.perimeter=2*(self.l+self.b)
    def display(self):
        print("Area of Rectangle:",self.area)
        print("Perimeter of Rectangle",self.perimeter)

print("Rectangle 1")
p1=Rectangle()
p1.display()
print("Rectangle 2")
p2=Rectangle()
p2.display()

if p1.area>p2.area:
    print("Rectangle 1 with Area", p1.area, "has larger area")
else:
    print("Rectangle 2 with Area",p2.area,"has larger area")