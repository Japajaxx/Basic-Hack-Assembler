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
    line_number = -1

    for i in lines:
        j = 0
        while i[j] == " ":
            j += 1
        if(not((i[j: j + 2] == "//") or (i[j] == "\n"))):
            line_number += 1

            if(i[j] == "@"):
                word = ""
                j += 1
                while (i[j] != "") and (i[j] != "\n"):
                    word += i[j]
                    j += 1
                if word.isdigit():
                    i = i.strip()
                    lines_new.append(i)
                elif word in key_words:
                    statement_assigner(lines_new, word)
                else:
                    key_words[word] = table_number
                    table_number += 1
                    statement_assigner(lines_new, word)
            elif(i[j] == "("):
                word = ""
                j += 1
                while (i[j] != ")"):
                    word += i[j]
                    j += 1
                if word not in key_words:
                    key_words[word] = line_number

            else:
                i = i.strip()
                lines_new.append(i)
        
    return lines_new

def code(parsed_lines):

    comp_table = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "!D": "0001101",
        "!A": "0110001",
        "-D": "0001111",
        "-A": "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",
        "M": "1110000",
        "!M": "1110001",
        "-M": "1110011",
        "M+1": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "D|M": "1010101"
    }

    dest_table = {
        "": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111"
    }

    jump_table = {
        "": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }
    
    binary_lines = []

    for i in parsed_lines:
        if(i[0] == "@"):
            binary_lines.append(bin(int(i[1:]))[2:].zfill(16))
        else:
            comp = ""
            dest = ""
            jump = ""

            if "=" in i:
                dest, i = i.split("=")
            if ";" in i:
                comp, jump = i.split(";")
            else:
                comp = i;
            binary_lines.append("111" + comp_table[comp] + dest_table[dest] + jump_table[jump])

    return binary_lines


def hack_assembler():
    # filename = input("Enter the name of the file you wish to assemble: ")
    parsed_lines = parser("Add.asm")
    finished = code(parsed_lines)

    for i in finished:
        print(i)


hack_assembler()

