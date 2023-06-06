class RF:
    def __init__(self):
        self.registers = {
        "000": "0000000000000000",
        "001": "0000000000000000",
        "010": "0000000000000000",
        "011": "0000000000000000",
        "100": "0000000000000000",
        "101": "0000000000000000",
        "110": "0000000000000000",
        "111": "0000000000000000",
        }
    def __str__(self):
        return f" r0:{self.registers['000']}, r1:{self.registers['001']}, r2:{self.registers['010']}, r3:{self.registers['011']}, r4:{self.registers['100']}, r5:{self.registers['101']}, r6:{self.registers['110']}, flags:{self.registers['111']}"
    
    def fetch_val(self,reg):
        return self.registers[reg]

    def mov_val(self,reg,data):
        self.registers[reg]=data
        
def int_to_7bit_binary(number):
  binary_string = bin(number)[2:]
  if len(binary_string) < 7:
    binary_string = "0" * (7 - len(binary_string)) + binary_string

  return binary_string

def binary_to_int(binary_string):
    binary_string = binary_string.zfill(7)  # Ensure the binary string has 7 bits
    decimal_number = int(binary_string, 2)
    return decimal_number

class MEM:
    def __init__(self):
        self.memory = {}
        for i in range(128):
            self.memory[int_to_7bit_binary(i)] = ""
            
class PC:
    def __init__(self):
        self.value = "0000000"
        self.link_reg = "0000000"
        self.address = int_to_7bit_binary(self.value)
    def increment(self):
        value = binary_to_int(self.value)+1
        self.value = int_to_7bit_binary(value)
        self.address = int_to_7bit_binary(self.value)
    def update_counter(self,value):
        self.link_reg=self.value
        self.value=value
class EE:
    def __init__(self):
            self.pc=PC()
            self.memory=MEM()
            self.regs=RF()
    def typeA(self,instruction):
        registers=self.regs # ditionary of regs / all registers
        # main dictionary  resigitry "000" : "0000000000000000"  
        if instruction[0:4]=="00000": #addition
            r1=instruction[7:10] # adress of registers
            r2=instruction[10:13]
            r3=instruction[13:16]
            flag="111"

            #self.regs.mov_val()
            #a=registers.fetch_val(r2)
            #b=registers.fetch_val(r3)
            #R3=a+b
            #int_to_7bit_binary(R3)
            b=binary_to_int(registers.fetch_val(r3))  #INTERGER VALUE of register 3
            a=binary_to_int(registers.fetch_val(r2))
            if a+b>=2**16:
                registers.mov_val(r1,"0000000")
                registers.mov_val(flag,"00000000000010000")
            else:
                registers.mov_val(r3,int_to_7bit_binary(a+b)) #moves binary no to r3
            

            
            
        if instruction[0:4]=="00110":   #multiplication
            r1=instruction[7:10]
            r2=instruction[10:13]
            r3=instruction[13:16]
            flag="111"
           
            b=binary_to_int(registers.fetch_val(r3))  #INTERGER VALUE of register 3
            a=binary_to_int(registers.fetch_val(r2))
            if a*b>=2**16:
                registers.mov_val(r1,"0000000")

                registers.mov_val(flag,"00000000000010000")
            else:
                registers.mov_val(r3,int_to_7bit_binary(a*b)) #moves binary no to r3
            
            
        if instruction[0:4]=="00001":   #subtraction
            r1=instruction[7:10]
            r2=instruction[10:13]
            r3=instruction[13:16]
            flag="111"
            b=binary_to_int(registers.fetch_val(r3))  #INTERGER VALUE of register 3
            a=binary_to_int(registers.fetch_val(r2))
            if a-b<0:
                registers.mov_val(r1,"0000000")

                registers.mov_val(flag,"00000000000010000")


            else:
                registers.mov_val(r3,int_to_7bit_binary(a-b)) #moves binary no to r3

        
             
        if instruction[0:4]=="01010":   #XOR
            r1=instruction[7:10]
            r2=instruction[10:13]
            r3=instruction[13:16]
            b=binary_to_int(registers.fetch_val(r3))  #INTERGER VALUE of register 3
            a=binary_to_int(registers.fetch_val(r2))
            registers.mov_val(r3,int_to_7bit_binary(a^b)) #moves binary no to r3
            
        if instruction[0:4]=="01100":   #AND
            r1=instruction[7:10]
            r2=instruction[10:13]
            r3=instruction[13:16]
            b=binary_to_int(registers.fetch_val(r3))  #INTERGER VALUE of register 3
            a=binary_to_int(registers.fetch_val(r2))
            registers.mov_val(r3,int_to_7bit_binary(a&b)) #moves binary no to r3
                   

    def typeB(self,instruction):
        registers=self.regs # dictionary of regs
        if (instruction[:5])=="00010":#mov reg1 imm
            # mov reg1 #imm
            # i[7:9]- reg   i[-7:]- value to be moved
            r=instruction[6:9]
            registers.mov_val(r,instruction[-7:])
            
        if (instruction[:5])=="01000":#rs reg1 imm
        # i[7:9]- reg   i[-7:]- value to be moved
            v = binary_to_int(instruction[9:])
            r1 = instruction[6:9]
            r = registers.fetch_val(instruction[6:9])
            r = binary_to_int(r)
            registers.mov_val(r1,int_to_7bit_binary(r<<v))
            
        if (instruction[:5])=="01001":#ls reg imm
        # i[7:9]- reg   i[-7:]- value to be moved
            v = binary_to_int(instruction[9:])
            r1 = instruction[6:9]
            r = registers.fetch_val(instruction[6:9])
            r = binary_to_int(r)
            registers.mov_val(r1,int_to_7bit_binary(r<<v))

    def typeC(self,instruction):
        registers=self.regs # dictionary of regs

        if (instruction[:5])=="00011":#mov reg1 reg2
        # i[-7:-4]- reg1    i[-3:]- reg2
            #self.regs.registers[i[-7:-4]]=self.regs.registers[i[-3:]]
            registers.mov_val(instruction[-6:-3],registers.fetch_val(instruction[-3:]))
        if (instruction[:5])=="00111":#div reg1 reg2
            if self.regs[instruction[-3:]]=="000000000000000":
                self.regs.registers["000"]="000000000000000"
                self.regs.registers["001"]="000000000000000"
                self.regs.registers["111"]="000000000001000"
            else:
                self.regs.registers["000"]=int_to_7bit_binary(binary_to_int(self.regs[instruction[-7:-4]])//binary_to_int(self.regs[instruction[-3:]]))
                self.regs.registers["001"]=int_to_7bit_binary(binary_to_int(self.regs[instruction[-7:-4]])%binary_to_int(self.regs[instruction[-3:]]))

        if (instruction[:5])=="01101":#not reg1 reg2
        # i[-7:-4]- reg1/3   i[-3:]- reg2/4
            a=self.regs.registers[instruction[-3:]]
            a=binary_to_int(a)
            a=~a
            a=int_to_7bit_binary(a)
            self.regs[instruction[-6:-3]]=a

        if (instruction[:5])=="01110":#cmp reg1 reg2
        # i[-6:-3]- reg1/3   i[-3:]- reg2/4
            if binary_to_int(self.regs.registers[instruction[-6:-3]])<binary_to_int(self.regs.registers[instruction[-3:]]):
                self.regs.registers["111"]="000000000000100"
                
            if binary_to_int(self.regs.registers[instruction[-6:-3]])>binary_to_int(self.regs.registers[instruction[-3:]]):
                self.regs.registers["111"]="000000000000010"
                
            if binary_to_int(self.regs.registers[instruction[-6:-3]])==binary_to_int(self.regs.registers[instruction[-3:]]):
                self.regs.registers["111"]="000000000000001"
        
    def typeD(self,instruction):
        registers=self.regs # dictionary of regs
        if(instruction[:5]=="00100"):
            value = self.memory.memory[instruction[9:]]
            registers.mov_val(instruction[6:9],value)
        if(instruction[:5]=="00101"):    
            value = self.regs.fetch_val[instruction[9:]]
            registers.mov_val(instruction[6:9],value)

    def typeE(self,instruction):
        op_dict=self.op_codes # dictionary of op_codes
        registers=self.regs # dictionary of regs
        
        if (instruction[:5])=="01111": # jmp to mem_addr -> Type E
            # pc = pc_value()
            self.pc.update_counter(instruction[-7:])
        if (instruction[:5])=="11100": # jlt to mem_addr -> Type E
            if registers.registers["111"] =="000000000000100":
                self.pc.update_counter(instruction[-7:])
            
        if (instruction[:5])=="11101": # jgt to mem_addr -> Type E
            if registers.registers["111"] =="000000000000010":
                self.pc.update_counter(instruction[-7:])
            
        if (instruction[:5])=="11111": # je to mem_addr -> Type E
            if registers.registers["111"] =="000000000000001":
                self.pc.update_counter(instruction[-7:])
                
    def typeFA(self,instruction):
        registers=self.regs # dictionary of regs
    
    def typeFB(self,instruction):
        registers=self.regs # dictionary of regs
    
    def execute(self,instruction):
        self.typeA(instruction)
        self.typeB(instruction)
        self.typeC(instruction)
        self.typeD(instruction)
        self.typeE(instruction)
        self.typeFA(instruction)
        self.typeFB(instruction)
        self.pc.increment()
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
