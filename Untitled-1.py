def find_longest_word(list1 , n):
    result = []
    for i in list1:
        if len(i)> n :
            result.append(i)
    return result
    
list1 = (input("Enter elements ").split(" "))
n = int(input("Enter the length of word "))
print(find_longest_word(list1 , n))