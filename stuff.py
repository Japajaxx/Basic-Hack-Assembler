key_words = {"R0": 0,
             "R1": 1,
             "R2": 2,
             "R3": 3,
             "R4": 4,
             "R5": 5,
             "R6": 6,
             "R7": 7,
             "R8": 8,
             "R9": 9,
             "R10": 10,
             "R11": 11,
             "R12": 12,
             "R13": 13,
             "R14": 14,
             "R15": 15,
             "SCREEN": 16384,
             "KBD": 24576,
             "SP": 0,
             "LCL": 1,
             "ARG": 2,
             "THIS": 3,
             "THAT": 4}


def statement_assigner(lines_new, word):
    lines_new.append("@" + str(key_words[word]))


def parser(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    lines_new = []
    table_number = 16

    for i in lines:
        j = 0

        while i[j] == " ":
            j += 1
        if(not((i[j: j + 2] == "//") or (i[j] == "\n"))):
            # Statements
            if(i[j] == "@"):
                word = ""
                j += 1
                while (i[j] != "") and (i[j] != "\n"):
                    word += i[j]
                    j += 1
                if word.isdigit():
                    pass
                elif word in key_words:
                    statement_assigner(lines_new, word)
                else:
                    key_words[word] = table_number
                    table_number += 1;
                    statement_assigner(lines_new, word)
            # None
            else:
                i = i.strip()
                lines_new.append(i)
        
    return lines_new


def hack_assembler():
    lines_new = parser("Max.asm")
    print(lines_new)


hack_assembler()

