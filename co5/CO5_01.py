f1=open("secfile.txt","w")
f1.write("This is my first file in python.\n want to work with files \n This is my third line")
f1=open("secfile.txt","r")
ff=f1.readlines()
print(ff)


