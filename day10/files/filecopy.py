with open("sample.txt") as f:
    lines = f.readlines()

with open("copy.txt", "w") as f1:
    f1.writelines(lines)
