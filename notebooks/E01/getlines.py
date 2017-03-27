from time import asctime
print(asctime())
line_no = 1
line = input("**Enter a line of text:\n")
while line:
    print("line", line_no, ":", line)
    line_no += 1
    line = input("**Enter another line of text:\n")
