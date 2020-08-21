import sys
from hack_parser import parser, code
from pathlib import Path

file_path = sys.argv[1]

SYMBOL_TABLE = {}

# Adding predefined symbols
with open("predefined.txt", "r") as pre_symbol_file:
    for line in pre_symbol_file:
        label, ram_address = tuple(line.rstrip("\n").split(" "))
        # Adding to the hash map
        SYMBOL_TABLE[label] = ram_address

# First Pass

# For tracking ROM Adress
n = 0 

# Initialize parser
asm_parser = parser.Parser(file_path)

while asm_parser.has_more_commands():
    if asm_parser.command_type() == "L_COMMAND":
        SYMBOL_TABLE[asm_parser.symbol()] = str(n)
    else:
        # Increment ROM address (line number in .hack file)
        n += 1

    # Move to the next command
    asm_parser.advance()

# Prepare for second pass
asm_parser.reset_to_begin()
asm_code = code.Code()

# For allocating memory address to symbols
ram_alloc_address = 16

out_file = Path(file_path).with_suffix(".hack")

with out_file.open("w") as out_f:
    # Until all the commands are exhausted
    while asm_parser.has_more_commands():
        if asm_parser.command_type() == "A_COMMAND":
            a_sym = asm_parser.symbol()
            # Is the symbol a number?
            try:
                int(a_sym)
            except ValueError as e:
                # Not a number
                # Process the symbol
                if a_sym in SYMBOL_TABLE:
                    a_sym = SYMBOL_TABLE[a_sym]
                else:
                    SYMBOL_TABLE[a_sym] = str(ram_alloc_address)
                    a_sym = str(ram_alloc_address)
                    ram_alloc_address += 1
            
            print(asm_code.handle_a_ins(a_sym), file=out_f)

        elif asm_parser.command_type() == "C_COMMAND":
            # Find the c, d and j feilds
            asm_parser.tokenize()
            cp = asm_parser.get_comp()
            dt = asm_parser.get_dest()
            jp = asm_parser.get_jump()

            ins_code = asm_code.handle_c_instruction(cp, dt, jp)
            print(ins_code, file=out_f)
        
        # Move forward
        asm_parser.advance()
