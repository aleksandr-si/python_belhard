a=input('enter first val:')
b=input('enter sec val:')


def nod_finder(a,b):
    val_list=[a,b]
    val_list.sort()
    # print(val_list)
    result=val_list[1]-val_list[0]

    if result==0:
        print(val_list[1])
    else:
        nod_finder(val_list[0],result)

nod_finder(int(a),int(b))
