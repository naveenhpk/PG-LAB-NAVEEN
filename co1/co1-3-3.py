string=str(input("enter the string"))
print("original string:",string)
print("vowels are:",end=" ")
for i in string:
    if i in 'aeiouAEIOU':
        print([i],end=" ")