# Parser class: Parses and tokenizes the input file
class Parser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.current_command_index = 0
        self.commands = None
        self.process_file()   

    def process_file(self):
        with open(self.file_path, "r") as f:
            lines = f.readlines()
            commands = filter(select, map(clean, lines))
            self.commands = list(commands)

    def has_more_commands(self):
        return self.current_command_index < len(self.commands)

    def advance(self):
        self.current_command_index += 1
    
    def command_type(self):
        if self.get_current_command().startswith("@"):
            return "A_COMMAND"
        elif self.get_current_command().startswith("("):
            return "L_COMMAND"
        else:
            return "C_COMMAND"

    def get_current_command(self):
        return self.commands[self.current_command_index]

    def get_dest(self):
        return self.dest

    def get_comp(self):
        return self.comp

    def get_jump(self):
        return self.jump

    def symbol(self):
        if self.command_type() == "A_COMMAND":
            return self.get_current_command()[1:]
        elif self.command_type() == "L_COMMAND":
            return self.get_current_command()[1:-1]

    def tokenize(self):
        self.jump = None
        self.comp = None
        self.dest = None

        tokens = self.get_current_command().split("=")

        if len(tokens) == 1:
            tokens = tokens[0].split(";")
            self.comp = tokens[0]
            self.jump = tokens[1]

        elif len(tokens) == 2:
            self.dest = tokens[0]
            tokens = tokens[1].split(";")

            if len(tokens) == 1:
                self.comp = tokens[0]
            elif len(tokens) == 2:
                self.comp = tokens[0]
                self.jump = tokens[1]

def clean(line):
    # Handeling inline comments
    if "//" in line:
        line = line[:line.index("//")]
    
    # Newline characters
    line = line.rstrip("\n")
    
    # Remove whitespaces
    line = line.replace(" ", "")

    # return cleaned line
    return line

def select(line):
    # Remove comment lines
    if line.startswith("//"):
        return False
    
    # Remove empty lines
    if line == "":
        return False
    
    return True


# TESTING
if __name__ == "__main__":
    p = Parser("temp.asm")

    while p.has_more_commands():
        print(p.get_current_command())
        if p.command_type() == "C_COMMAND":
            p.tokenize()
            print(p.get_dest(), p.get_comp(), p.get_jump())
        p.advance()