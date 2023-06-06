f=open("input",'r')
a=f.readlines()
# print(a)
machine_code=[]

# __________________________IMPORT________________________
# import Dictionaries as dic
import Assembler.disctionaries as dic
import Functions as func
import Components as com
for i in a:
    machine_code.append(i[:-1])

# for i in machine_code:
#     print(i)
"""
00000000001 lable : myloop smp
00000000010 add
00000000011 sub
00000000100 mul
00000000101 jmp myloop
00000000001 cmp
00000000010 add
"""
halt=False #altered
pc_dict={} #altered
pc=0 #altered
# for i in machine_code:
while not halt: #altered
    i=machine_code[pc]
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
    
    if (i[:5])=="00100 ": # load from variable to reg -> Type D
        dic.reg[i[-10:-7]]= com.MEM.memory[i[-7:]]
        print(f'{func.to_binary(machine_code.index(i),7)} 000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
    
    if (i[:5])=="00101 ": # Store from reg to variable -> Type D
        com.MEM.memory[i[-7:]] = dic.reg[i[-10:-7]]
        print(f'{func.to_binary(machine_code.index(i),7)} 000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
    
    if (i[:5])=="01111 ": # jmp to mem_addr -> Type E
        # pc = pc_value()
        pc = dic.labels[i[-7:]]
        print(f'{func.to_binary(machine_code.index(i),7)} 000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
        continue
    if (i[:5])=="11100 ": # jlt to mem_addr -> Type E
        
        if dic.reg["111"][-3] =="1":
            
            pc = dic.labels[i[-7:]]
            continue
        print(f'{func.to_binary(machine_code.index(i),7)} 000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
        
    if (i[:5])=="11101 ": # jgt to mem_addr -> Type E
        if dic.reg["111"][-2] =="1":
            pc = dic.labels[i[-7:]]
            continue
        print(f'{func.to_binary(machine_code.index(i),7)} 000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
       
    if (i[:5])=="11111 ": # je to mem_addr -> Type E
        if dic.reg["111"][-1] =="1":
            pc = dic.labels[i[-7:]]
            continue
        print(f'{func.to_binary(machine_code.index(i),7)} 000000000{dic.reg["000"]} 000000000{dic.reg["001"]} 000000000{dic.reg["010"]} 000000000{dic.reg["011"]} 000000000{dic.reg["100"]} 000000000{dic.reg["101"]} 000000000{dic.reg["110"]} 000000000{dic.reg["111"]} ')
        
    if (i[:5])=="11010 ": #type F hlt
        halt=True
    pc+=1

# print(dic.reg)