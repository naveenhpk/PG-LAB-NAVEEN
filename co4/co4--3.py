class rectangle:
    def __init__(self):
        self.__length=int(input("Enter the length: "))
        self.__width=int(input("Enter the breadth: "))
    def __lt__(self,a1):
        area1=self.__length*self.__width
        area2=a1.__length*a1.__width
        if(area1<area2):
            return(True)
        else:
            return(False)     
print("RECTANGLE 1")
r1=rectangle()
print("RECTANGLE 2")
r2=rectangle()
if(r1<r2):
    print("Rectangle 2 is larger!!")
else:
    print("Rectangle 1 is larger!!")
