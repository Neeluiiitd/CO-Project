class RF:
    def __init__(self):
        self.registers = {
        "000": "",
        "001": "",
        "010": "",
        "011": "",
        "100": "",
        "101": "",
        "110": "",
        "111": "",
        }
    def __str__(self):
        return f" r0:{self.registers['000']}, r1:{self.registers['001']}, r2:{self.registers['010']}, r3:{self.registers['011']}, r4:{self.registers['100']}, r5:{self.registers['101']}, r6:{self.registers['110']}, flags:{self.registers['111']}"
    def add_val(self,val,reg):
        self.registers[val]=reg
    def add_reg_content(self,r1,r2):
        self.registers[r1]=self.registers[r2]

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
        self.link_reg = "0000000"
        self.address = int_to_7bit_binary(self.value)
    def increment(self):
        self.value +=1
        self.address = int_to_7bit_binary(self.value)
    def update_counter(self,value):
        self.link_reg=value
class EE:
    def __init__(self,pc,mem,reg):
            self.op_codes = {
            "00000": "add",
            "00001": "sub",
            "00110": "mul",
            "00111": "div",
            "01010": "xor",
            "01011": "or",
            "01100": "and",
            "01101": "not",
            "01110": "cmp",
            "00010": "mov",
            "00011": "mov",
            "00100": "ld",
            "00101": "st",
            "01000": "rs",
            "01001": "ls",
            "01111": "jmp",
            "11100": "jlt",
            "11101": "jgt",
            "11111": "je",
            "11010": "hlt",
            "10000": "addf",
            "10001": "subf",
            "10010": "movf",}
            self.pc=pc
            self.memory=mem
            self.regs=reg
            self.op_ls={"typeA" : [] , "typeB" : [] ,"typeC" : [] ,"typeD" : [] ,"typeE" : [], "typeF" : []}
    def typeA(self,instruction):
        return
    
    def typeB(self,instruction):
        return
    
    def typeC(self,instruction):
        return
    
    def typeD(self,instruction):
        return
    
    def typeE(self,instruction):
        return
    
    def execute(self,instruction):
        return
    """def decode_execute(self,code):
        for i in code:
            if (i[:5])=="00010":
            # mov reg1 #imm
            # i[7:9]- reg   i[-7:]- value to be moved
                dic.reg[i[6:9]]= i[-7:]
            print(f'{func.to_binary(machine_code.index(i),7)} 000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')

            if (i[:5])=="00011":
            # i[-7:-4]- reg1    i[-3:]- reg2
                dic.reg[i[-7:-4]]=dic.reg[i[-3:]]
                print(f'{func.to_binary(machine_code.index(i),7)} 000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
        
            if (i[:5])=="00111 ":
            # i[-7:-4]- reg1/3   i[-3:]- reg2/4
                if dic.reg[i[-3:]]=="0":
                    dic.reg["000"]="0"
                    dic.reg["001"]="0"
                    dic.reg["111"]="000000000001000"
                    print(f'000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
                else:
                    dic.reg["000"]=(dic.reg[i[-7:-4]])//(dic.reg[i[-3:]])
                    dic.reg["001"]=(dic.reg[i[-7:-4]])%(dic.reg[i[-3:]])
                    print(f'000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')

            if (i[:5])=="01001 ":
                # i[7:9]- reg   i[-7:]- value to be moved
                str=""
                str+=dic.reg[i[-7:-4]]
                str=str[1:]
                str+="0"

            if (i[:5])=="01110 ":
                # i[-7:-4]- reg1/3   i[-3:]- reg2/4
                if dic.reg[i[-7:-4]]<dic.reg[i[-3:]]:
                    dic.reg["111"]="000000000000100"
                    print(f'000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
                if dic.reg[i[-7:-4]]>dic.reg[i[-3:]]:
                    dic.reg["111"]="000000000000010"
                    print(f'000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
                if dic.reg[i[-7:-4]]==dic.reg[i[-3:]]:
                    dic.reg["111"]="000000000000001"
                    print(f'000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
"""
