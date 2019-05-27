arr = [10, 22, 233, 4, 55555, 45]
a = 0
b = 0
for name in arr:
    if name > arr[a]:
        a = arr.index(name)
    elif name < arr[b]:
        b = arr.index(name)
arr[-1] = arr[b]
arr[b] = 45
arr[0] = arr[a]
arr[a] = 10
print(arr)



