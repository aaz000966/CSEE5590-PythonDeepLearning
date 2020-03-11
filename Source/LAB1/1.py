# TODO
# Author: Team 8
# Usecase: Printing all possible subsets excluding null values

def SubsetsOf(MyList):
    # representing the algorithm using python
    elements = len(MyList)
    toReturn = []
    count = pow(2, elements)
    for i in range(1, count):
        temp = ""
        print("", end="")
        for j in range(0, elements):
            if (i & (1 << j)) > 0:
                temp += (str(MyList[j]) + ",")
        if temp.endswith(","):  # basically to remove the comma from the temp string
            temp = temp[:-1]
        listTemp = list(temp.split(","))  # taking back the String to a list
        if listTemp not in toReturn:  # Add to the returned list if not exist
            toReturn.append(listTemp)
    return toReturn


def main():
    myList = SubsetsOf([1, 2, 2])  # The problem given in the lab task
    print(myList)


if __name__ == '__main__':
    main()
