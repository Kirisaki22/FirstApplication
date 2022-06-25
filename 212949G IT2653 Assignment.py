hotel_list= [['john tan','treasure of raffles',1000,3],
             ['sally tang','grandeur of raffles',1200,6],
             ['mary hathaway','journey to wholeness',1100,4],
             ['rachel wong','raffles summer escapes',1600,3],
             ['elliott lim','rise and shine',1450,2],
             ['alison ng','short and suite',1950,8]]
pos = 0
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

def selectionSort(array):
    n = len(array)
    for i in range(n - 1):
        curr = i
        for j in range(i + 1, n):
            if (array[j][1] < array[curr][1]):
                curr = j
        if curr != i:
            tmp = array[i]
            array[i] = array[curr]
            array[curr] = tmp


def insertionSort(hotel_list):
    for i in range(1, len(hotel_list)):
        key = hotel_list[i]
        j = i - 1
        while j >= 0 and key[-2] < hotel_list[j][-2]:
            hotel_list[j + 1] = hotel_list[j]
            j -= 1
        hotel_list[j + 1] = key



answer = input("Hello! Type S to Start: ")
answer = answer.upper()
if answer == "S":
    while True:
        print("=================================")
        print("Raffles Hotel Staycation Records")
        print("=================================")
        print("Select from following choices to continue:")
        print("1. Display all records")
        print("2. Sort record by Customer Name using Bubble sort")
        print("3. Sort record by Package Name using Selection sort")
        print("4. Sort record by Package Cost using Insertion sort")
        print("5. Search record by Customer Name using Linear Search and update record")
        print("6. Search record by Package Name using Binary Search and update record")
        print("7. List records range from $x to $y")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            print(hotel_list)
        elif choice == '2':
            bubble_sort(hotel_list)
            print(hotel_list)
        elif choice == '3':
            selectionSort(hotel_list)
            print(hotel_list)
        elif choice == '4':
            insertionSort(hotel_list)
            print(hotel_list)
        elif choice == '5':
            def linearsearch(val, target):
                n = len(val)
                for i in range(n):
                    if val[i][0] == target:
                        print('name have been found')
                        n = (input("what do you want to update: ").lower())
                        if n == 'name':
                            nn = input("type new name: ")
                            val[i][0] = nn
                            print(hotel_list)
                        elif n == 'package name':
                            pn = input("type new package name: ")
                            val[i][1] = pn
                            print(hotel_list)
                        elif n == 'package cost':
                            pc = input("type new package cost: ")
                            val[i][2] = pc
                            print(hotel_list)
                        elif n == 'num pax':
                            np = input("type new num pax: ")
                            val[i][3] = np
                            print(hotel_list)
                        else:
                            print("Invalid option")
                        return i
                print('name cannot been found')
                return -1

            x = linearsearch(hotel_list, input('Enter the customer name to search: ').lower())
        elif choice == '6':
            def binarySearch(array, target):
                low = 0
                high = len(array) - 1
                while low <= high:
                    mid = (high + low) // 2
                    n = len(array)
                    for i in range(n):
                        if array[i][1] == target:
                            print('package name found')
                            n = (input("what do you want to update: ").lower())
                            if n == 'name':
                                nn = input("type new name: ")
                                array[i][0] = nn
                                print(hotel_list)
                            elif n == 'package name':
                                pc = input("type new package name: ")
                                array[i][1] = pc
                                print(hotel_list)
                            elif n == 'package cost':
                                pc = input("type new package cost: ")
                                array[i][2] = pc
                                print(hotel_list)
                            elif n == 'num pax':
                                pc = input("type new num pax: ")
                                array[i][3] = pc
                                print(hotel_list)
                            else:
                                print("Invalid option")
                            return True
                        else:
                            print('package name found')
                    return False
            binarySearch(hotel_list, input('Enter the package name to search: '))
            selectionSort(hotel_list)
        elif choice == '7':
            try:
                range_x = int(input("Enter first range: "))
                range_y = int(input("Enter second range: "))
                for j in range(len(hotel_list)):
                    if (hotel_list[j][2] >= range_x) and (hotel_list[j][2] <= range_y):
                        print(hotel_list[j][0], hotel_list[j][1],hotel_list[j][2], hotel_list[j][3])
            except ValueError:
                print("Input is not a number")
        elif choice == '0':
            break
        else:
            break
else:
    print("Error")
