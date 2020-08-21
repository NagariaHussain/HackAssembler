# comp (a, c1, c2, c3, c4, c5, c6) feild translation mappings
COMP_MAPPINGS = {
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "M":   "1110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "!M":  "1110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "-M":  "1110011",
    "D+1": "0011111",
    "A+1": "0011111",
    "M+1": "1011111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101",
}

# jump (j1, j2, j3) feild translation mappings
JUMP_MAPPINGS = {
    None: "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

# dest (d1, d2, d3) feild translation mappings
DEST_MAPPINGS = {
    None: "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}

# Predefined symbols tabel
# PREDEFINED = {}

# with open("predefined.txt", "r") as pre_symbol_file:
#     for line in pre_symbol_file:
#         label, ram_address = tuple(line.rstrip("\n").split(" "))
#         # Adding to the hash map
#         PREDEFINED[label] = ram_address

# Code class: Carries out the translation
class Code:
    def handle_a_ins(self, symbol):
        return "0{:0>15b}".format(int(symbol))
    
    def handle_c_instruction(self, cp, dt, jp):
        return "111{}{}{}".format(
            COMP_MAPPINGS[cp],
            DEST_MAPPINGS[dt],
            JUMP_MAPPINGS[jp]
        )
    


