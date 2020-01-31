numberOfStudents = int(input("How many students? "))
listOfWeightsInLb = []
listOfWeightsInKG = []
# 0.45359237
temp = 0

for studentWeight in range(int(numberOfStudents)):
    temp = float(input("weight of student {} ".format(studentWeight + 1)))
    listOfWeightsInLb.append(temp)


listOfWeightsInKG = [int(i * 0.45359237) for i in listOfWeightsInLb]


print("weights in KG: ", listOfWeightsInLb)

print("weights in KG: ", listOfWeightsInKG)


def string_alternative(given="hello world"):
    flag = True
    output = ""
    for char in given:
        if flag:
            output += char
            flag = 0
        else:
            flag = 1

    print(output)


stringToAlter = input("write a string to return every other char: ")
string_alternative(stringToAlter)

infile = open("text.txt","r")
KeyValues = dict()

line = infile.readline()
while line != "":

    for word in line.split(" "):
        if word.strip() in KeyValues:
            KeyValues[word] += 1
        else:
            KeyValues[word.strip()] = 1
    line = infile.readline()

print(KeyValues)
