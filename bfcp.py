import sys, msvcrt

try: inputfile = str(sys.argv[1])
except: IndexError = inputfile = 'main.bf'

class program():

    def __init__(self):
        self.tape = [0]
        self.selected = 0
        self.commands = []
        self.command_counter = 0
        self.instructions = {
            '>': self.move_r,
            '<': self.move_l,
            '+': self.inc,
            '-': self.red,
            ',': self.take_input,
            '.': self.output,
            '[': self.start_loop,
            ']': self.end_loop
            }

    def add_commands(self, code: str):
        self.commands.extend([i for i in code])

    def move_r(self):
        self.selected += 1
        if len(self.tape) - 1 < self.selected:
            self.tape.append(0)

    def move_l(self):
        self.selected -= 1
        if self.selected < 0:
            self.selected += 1
            self.tape.insert(0, 0)

    def inc(self):
        self.tape[self.selected] += 1
        if self.tape[self.selected] > 255:
            self.tape[self.selected] = 0

    def red(self):
        self.tape[self.selected] -= 1
        if self.tape[self.selected] < 0:
            self.tape[self.selected] = 255

    def take_input(self):
        val = ord(msvcrt.getch())
        self.tape[self.selected] = val

    def output(self):
        val = self.tape[self.selected]
        print(chr(val), end="")

    def start_loop(self):
        if self.tape[self.selected] == 0:
            bracket_counter = 1
            while self.commands[self.command_counter] != ']' or bracket_counter != 0:
                self.command_counter += 1
                if self.commands[self.command_counter] == '[':
                    bracket_counter += 1
                elif self.commands[self.command_counter] == ']':
                    bracket_counter -= 1

    def end_loop(self):
        if self.tape[self.selected] != 0:
            bracket_counter = 1
            while self.commands[self.command_counter] != '[' or bracket_counter != 0:
                self.command_counter -= 1
                if self.commands[self.command_counter] == ']':
                    bracket_counter += 1
                elif self.commands[self.command_counter] == '[':
                    bracket_counter -= 1

    def start(self):
        while self.command_counter < len(self.commands):
            if self.commands[self.command_counter] not in self.instructions.keys():
                self.command_counter += 1
                continue
            self.instructions[self.commands[self.command_counter]]()
            self.command_counter += 1

if __name__ == '__main__':
    code = ''
    with open(inputfile, 'r') as file:
        code = file.read()

    prog = program()
    prog.add_commands(code)
    prog.start()