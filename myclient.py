import mypkg.mymode 


filename = input("Enter the filename: ")
lines = mypkg.mymode.count_lines(filename)
chars = mypkg.mymode.count_char(filename)
words = mypkg.mymode.count_words(filename)
print(f"Lines: {lines}, Characters: {chars}, Words: {words}")

