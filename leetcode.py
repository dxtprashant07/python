# class Solution:
#     def myAtoi(self, s: str) -> int:
#         s =s.strip()
#         if  len(s)== 0:  #to check is string is empty
#             return 0
#         if s[0] == "-":
#             sign = -1
#             s = s[1:]
#         elif s[0] == "+":
#             sign = 1
#             s = s[1:]
#         else:
#             sign = 1
#         num = 0
#         for i in s:
#             if i.isdigit():
#                 num = num * 10 + int(i)
#             else:
#                 break
#         num *= sign
#         if num <= -2**31:
#             return -2**31
#         if num > 2**31 - 1:
#             return 2**31 - 1
        
#         return num




# def dev():
#     if n %2 ==0:
#         return "even"
# n = int(input())
# print(dev())

# def dev(m):
#     m =m**2
#     return m
# m = int(input())
# print(dev(m))

# def dev(m):
#     if m%2 == 0:
#         print ("even")
#     else :
#         print("odd")

# m = int(input())
# dev(m)

# def dev(m,n):
#     sum =m+n
#     print(sum)
# m = int(input())
# n = int(input())
# dev(m,n)

# import math
# def circle(r):
#     area = math.pi *r**2
#     return area
#     # print(area)
# n = int(input())
# m = circle(n)
# print(m)


# def dev(n):
#     if n == 0 or n == 1:
#         return 1 
#     else:
#        return n * dev(n-1)
    
# n = int(input())
# rec = dev(n)
# print(rec)


# import math
# def is_prime(n):
#     if n < 1:
#         return False
#     elif n == 2:
#         return  False
#     else:
#         for i in range(2 , int(math.sqrt(n))+1):
#             if n % i == 0:
#                 return False
#     return True
# n = int(input())

# m = is_prime(n)
# print(m)


# def dev(string):
#     string = string[::-1]
#     print(string)
# stri = input()
# dev(stri)

# def dev(s):
#     s = set(s)
#     s = list(s)
#     return s
# m = [11,2,4,5,4,3,4,6,7]
# n= dev(m)
# print(n)


# def word(s):
#     s = s.replace(" ","")
#     n = len(s)
#     print(n)
# s = input()
# word (s)

# def fobi(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fobi(n-1) +fobi(n-2)
        
# n = int(input())
# for i in range(n):
#     print(fobi(i), end=" ")

# def dev(list1):
#     max1 = max(list1)
#     min1 = min(list1)
#     return max1, min1
# list1 = [1,2,3,42,2,4,22,4]
# print(dev(list1))


# def search_insert(nums , target):
#     for i in range(len(nums)):
#         if nums[i] > target:
#             nums.insert(i , target)
#             return nums
# nums = [1,3,5,6]
# target = 4
# print(search_insert(nums , target))

# list1 = [(1,2) , (3,4) , (5,600) , (7,8)]
# list1.sort(key = lambda x : x[1])
# print(list1)

# list1 = ["apple" , "banana" , "cherry" , "kiwi" , "mango"]
# list1.sort(key = lambda x : len(x))
# print(list1)

# string = input()
# string = string.split(" ")
# string.sort(key = lambda x : x)
# print(string)

# class display_info:
#     def __init__(self , brand, model):
#         self.model = model
#         self.brand = brand

#     def brand1(self):
#         print(f"Brand : {self.brand}")
#     def model1(self):
#         print(f"Model : {self.model}")
# car1 = display_info("BMW" , "X5")
# car1.brand1()

