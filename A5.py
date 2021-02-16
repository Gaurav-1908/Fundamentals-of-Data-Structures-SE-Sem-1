"""Write a Python program to compute following operations on String:
	a)To display word with the longest length.
	b)To determines the frequency of occurrence of particular character in the string.
	c)To check whether given string is palindrome or not. 
	d)To display index of first appearance of the substring. To count the occurrences of each word in a given string. """

def length(x):
    leng = 0
    for _ in x:
        leng += 1
    return leng
    
def sorting(x):
    length = 0
    for i in x:
        length += 1 
    for i in range(length):
        for j in range(i + 1, length):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return x

def longest_string(string1):
    l = []
    for i in string1:
        n = len(i)
        l.append(n)
    l = sorting(l)
    return(l[-1])

def char_Search(string1):
    frequency = {}
    for i in string1:
        for j in i:
            frequency[j] = frequency.get(j, 0) + 1
    z = input("Enter the charecter you want to search for ? ") 
    for key, value in frequency.items(): 
         if z == key: 
             print("The Charecter is repeated: ", value, " times")
             break
         else:
            print("Charecter not found")

def char_occurence(string1):
    frequency = {}
    for i in string1:
        for j in i:
            frequency[j] = frequency.get(j, 0) + 1
    for key, value in frequency.items(): 
             print("The letter: " , key, " is repeated: ", value, " times \n")

def palindrome (string):
    string = string.lower()
    for _ in string :
        rev_string = string[::-1]
    if string == rev_string:
        print("It is a palindrome")
    else:
        print("Not a palindrome")

def main():
    Str = input("Enter first string: ")
    str_list = Str.split()
    char_Search(str_list)
    char_occurence(str_list)
    palindrome(Str)

main()
