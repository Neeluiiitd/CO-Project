class RF:
    def __init__(self):
        self.registers = {
        "000": {"r0" : ""},
        "001": {"r1" : ""},
        "010": {"r2" : ""},
        "011": {"r3" : ""},
        "100": {"r4" : ""},
        "101": {"r5" : ""},
        "110": {"r6" : ""},
        "111": {"flags" : ""},
        }

def int_to_7bit_binary(number):
  binary_string = bin(number)[2:]
  if len(binary_string) < 7:
    binary_string = "0" * (7 - len(binary_string)) + binary_string

  return binary_string
        
class MEM:
    def __init__(self):
        self.memory = {}
        for i in range(128):
            self.memory[int_to_7bit_binary(i)] = ""
            
class PC:
    def __init__(self):
        self.value = 0
        self.address = int_to_7bit_binary(self.value)
    def increment(self):
        self.value +=1
        self.address = int_to_7bit_binary(self.value)
        
class EE:
    def __init__(self):
        