def parse(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()
    return lines

lines = parse("Add.asm")

lines_new = []

for i in lines:
    j = 0
    while i[j] == " ":
        j+=1
    if(not((i[j:(j+2)] == "//") or (i[j:(j+2)] == "\n"))):
        i = i.strip()
        lines_new.append(i)

print(lines_new)

