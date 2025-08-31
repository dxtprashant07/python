from mypkg.mymode import *

filename = input("Enter the filename: ")
lines = count_lines(filename)
chars = count_char(filename)
words = count_words(filename)
print(f"Lines: {lines}, Characters: {chars}, Words: {words}")