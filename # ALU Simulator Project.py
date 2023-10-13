# ALU Simulator Project

# Instruction sent from software (machine code) to hardware (CPU(ALU)):

# OPCODE Table:
# +-----------|--------+
# |   Name    | OPCODE |
# |-----------|--------|
# | ADD       | 000001 |
# | SUBTRACT  | 000010 |
# | MULTIPLY  | 000011 |
# | DIVIDE    | 000100 |
# | LOAD      | 000101 |
# | STORE     | 000110 |
# +--------------------+

class ALU:

    def __init__(self, name):
        self.name = name
        self.number_registers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.numbers_index = 1
        self.output = ''

    def update_output(self, update):
        self.output = update
        print(self.output)

    def store_value(self, value):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = (int(value))
        print(f"{int(value)} was stored at {self.numbers_index}")
        self.numbers_index += 1

    def load_value(self, address):
        index = int(address, 2)
        int_value = int(self.number_registers[index])
        return int_value
    
    def add(self, num1, num2):
        num11 = self.load_value(num1) 
        num22 = self.load_value(num2)
        calculated_value = num11 + num22
        return calculated_value

    def multiply(self, num1, num2):
        num11 = self.load_value(num1) 
        num22 = self.load_value(num2)
        calculated_value = num11 * num22
        return calculated_value
    
    def subtract(self, num1, num2):
        num11 = self.load_value(num1) 
        num22 = self.load_value(num2)
        calculated_value = num11 - num22
        return calculated_value
    
    def divide(self, num1, num2):
        num11 = self.load_value(num1) 
        num22 = self.load_value(num2)
        if num22 == 0:
            print(f"Division by 0 error")
        else:
            calculated_value = num11 / num22
            return calculated_value


    def binary_reader(self, binary):
        if len(binary) > 32:
            self.output = 'Invalid Input'
            return
        opcode = binary[0:6]
        source_one = binary[6 : 11]
        source_two = binary[11 : 16]
        store = binary[16 : 26]
        function_code = binary[26:]
        if opcode == '000001':
            self.store_value(store)
            return
        elif opcode != '000000':
            self.update_output('Invalid OPCODE')
            return
        result = 0
        if (function_code == '100000'):
            result = self.add(source_one, source_two)
        elif (function_code == '100010'):
            result = self.subtract(source_one, source_two)
        elif (function_code == '011000'):
            result = self.multiply(source_one, source_two)
        elif (function_code == '011010'):
            result = self.divide(source_one, source_two)
        else:
            self.update_output("Invalid Function")
            return
        self.store_value(result)
        self.update_output(f'The result is {result}')


CPU_Simulator = ALU('Simulator')


CPU_Simulator.binary_reader("00000100000000000000000101000000")
CPU_Simulator.binary_reader("00000100000000000000001010000000")
CPU_Simulator.binary_reader("00000000001000100000000000100000")



