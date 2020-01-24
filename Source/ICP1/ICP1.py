
inString = input("Write a string: ")
inNo = input("How many characters to delete? ")
newString = inString[int(inNo):]
print("result after processing: ", newString)
print("reversed copy: ", newString[::-1])
inNo2 = int(input("Now, enter two numbers for addition "))
inNo3 = int(input())
print("The result= ", inNo2 + inNo3)

inString = input("Enter a sentence with the word \"python\" in it: ")
print(inString.replace("python", "pythons"))
