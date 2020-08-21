import sys
from hack_parser import parser, code
from pathlib import Path

file_path = sys.argv[1]


asm_parser = parser.Parser(file_path)
asm_code = code.Code()

out_file = Path(file_path).with_suffix(".hack")

with out_file.open("w") as out_f:
    # Until all the commands are exhausted
    while asm_parser.has_more_commands():
        if asm_parser.command_type() == "A_COMMAND":
            a_sym = asm_parser.symbol()
            print(asm_code.handle_a_ins(a_sym), file=out_f)

        elif asm_parser.command_type() == "C_COMMAND":
            # Find the c, d and j feilds
            asm_parser.tokenize()
            cp = asm_parser.get_comp()
            dt = asm_parser.get_dest()
            jp = asm_parser.get_jump()

            ins_code = asm_code.handle_c_instruction(cp, dt, jp)
            print(ins_code, file=out_f)
        
        asm_parser.advance()
