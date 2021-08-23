


def numbers():
    mylist=[6, 8, 5, 9, 7, 2]
    mylist.sort()#sorting values in ascending order

    print(mylist)

    mylist.sort(reverse=True)#reverse sorting
    print(mylist)

    mytuple=(4, 5,6,('egg'))#Creating tuple and printing its contents
    print(mytuple)

if __name__ == '__main__':
    numbers()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
