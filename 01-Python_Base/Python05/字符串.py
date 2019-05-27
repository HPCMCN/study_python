x = "hsk hf jkls jkl"
b = "hskhfjklsjkl"
list1 = []
name1 = ""
for name in x:
    list1.append(name)
i = 0
while i < len(list1):
    if list1[i] == " ":
        del list1[i]
        continue
    i += 1
for name in list1:
    name1 += name
x = name1
print(x)