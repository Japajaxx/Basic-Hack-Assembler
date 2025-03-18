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


def parser(file_path):

    def remove_whitespace_and_labels():
        line_number = 0
        for i in lines:
            if i[0] != "\n":
                i = i.strip()
                if i[0] != "/":
                    i = i.strip()
                    if i[0] == "(":
                        word = i[1:-1]
                        if word not in key_words:
                            key_words[word] = line_number
                    else:
                        line_number += 1
                        lines_new.append(i)
    
    def symbols():
        table_number = 16
        for i in lines_new:
            if i[0] == "@":
                word = i[1:]
                if word.isdigit():
                    pass
                elif word in key_words:
                    lines_new[lines_new.index(i)] = "@" + str(key_words[word])
                else:
                    key_words[word] = table_number
                    table_number += 1
                    lines_new[lines_new.index(i)] = "@" + str(key_words[word])

    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    lines_new = []
    remove_whitespace_and_labels()
    symbols()

    return lines_new


def code(parsed_lines, filename):

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
    
    hack_file = open(filename + (".hack"), "a")
    j = 0

    for i in parsed_lines:
        if(i[0] == "@"):
            hack_file.write(bin(int(i[1:]))[2:].zfill(16))
        else:
            comp = ""
            dest = ""
            jump = ""

            if "=" in i:
                dest, i = i.split("=")
            if ";" in i:
                comp, jump = i.split(";")
            else:
                comp = i
            hack_file.write("111" + comp_table[comp] + dest_table[dest] + jump_table[jump])
        
        if j != len(parsed_lines) - 1:
            hack_file.write("\n")

        j += 1
    
    hack_file.close()


def hack_assembler():
    filename = input("Enter the name of the file you wish to assemble: ")
    parsed_lines = parser(filename + ".asm")
    code(parsed_lines, filename)

hack_assembler()

