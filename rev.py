def reverseString(str1):
    newstr=''
    length = len(str1)
    for i in range (-1,-length-1,-1):
        newstr += str1[i]
    return newstr

str1 =input("Enter a String")
strr= reverseString(str1)
print("The Original String is:", str1)
print("The reverse String is:", strr)         