def reserve(list):
    for i in range(0,int(len(list)/2)):
        other = len(list)-i-1
        temp =list[i]
        list[i]=list[other]
        list[other] = temp
    print(list)
my_list = [1,2,3,4,5]
reserve(my_list)