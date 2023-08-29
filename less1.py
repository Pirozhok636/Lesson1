list = [x for x in input()]

otv=1

while len(list) > 1:
    if list[0] == list[-1]:
        list.pop(0)
        list.pop(-1)
    else: 
        print(False)
        otv=0
        break
if otv == 1:
    print(True)