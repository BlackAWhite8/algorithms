list = [2,3,55,5,6,6,7,4,3,2,13,2,4,4,2,4,24,68,9]
list.sort()
target = 13

min =  0
max =  len(list)-1
while min != max:
    avarage = (min + max) // 2
    if list[avarage] == target:
        print("element situated in ", avarage,"case")
        break;
    elif list[avarage] > target:
        max = avarage

    elif list[avarage] < target:
        min = avarage

print (list)