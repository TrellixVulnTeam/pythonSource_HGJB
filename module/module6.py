import os

print("현재 운영체제 : ", os.name)
print("현재 폴더 : ", os.getcwd())
print("현재 폴더 내부의 요소: ", os.listdir())

with open("original.txt", "w") as f:
    f.write("hello")

#os.rename("original.txt","new.txt")


os.remove("new.txt")