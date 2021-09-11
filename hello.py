# h=open("hello.txt")
# test2=h.read()
# print(test2)

# h=open("hello.txt",'w')
# h.write("welcome")
# h.close()


# f=open("hello.txt",'r')
# test1=f.read()
# print(test1)


h=open("hello.txt",'a')
h.write("welcome to all")
h.close()

f=open("hello.txt",'r')
test1=f.read()
print(test1)

