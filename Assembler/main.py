"""
○ The opcode must be one of the supported mnemonic.
○ A register can be one of R0, R1, ... R6, and FLAGS.
○ A mem_addr in jump instructions must be a label.
○ A Imm must be a whole number <= 127 and >= 0.
○ A mem_addr in load and store must be a variable.

==============================================================================================
Assuming that the assembly codes are sepeareted by two lines in the main text file
==============================================================================================

"""
# custom fucntions and mudles being implemented.
import functions as fun
import disctionaries as dic
import operations as op
import sys
#necessary list

# list of assembly code

toexit = False

#main_program=fun.ins_return(f"/home/rijusmit-biswas/Desktop/Testing/CO_A_P1/Simple-Assembler/test4")
arg=[]
while True:
    try:
        stdin=input()
        arg.append(stdin)
    except:
         break
#ls=sys.stdin.
main_program=fun.split_input(arg)
exit = "__exit__"

if(main_program==[]):
    __name__= exit
    toexit = True
else:
    __name__="__main__"

if(toexit == False):


    # memmr address of instructions
    program_memory=fun.prg_mem(main_program)
    #necessary dictionaries

    # binary address of variables
    variables=fun.cr_var(main_program,program_memory)
    labels=fun.ad_dict(main_program,program_memory,variables)
    """-----------------------------------Don't touch this code------------------------------------"""
    for i,j in variables.items():
        for k in program_memory:
            if(k[0]==j):
                k[1]=i
    """-----------------------------------please---------------------------------------------------"""
    # print(program_memory)
    main_program=fun.rm_label(main_program)
    # print(main_program)
    a=dic.typeA
    b=dic.typeB
    c=dic.typeC
    d=dic.typeD
    e=dic.typeE
    f=dic.typeF
    program_counter=0
    set_of_mcode=[]
    set_of_errors=[]
        #structure of data-----------------------------------------------------------------------
        #["opcode",["arg1","arg2"]]
        #function to find flag register in assembly code

    for i in main_program:  
            if (i[0] not in dic.op_code and i[0]!="var"):
                    set_of_mcode.append("FC")
                    set_of_errors.append(f"Error at line {main_program.index(i)+1+len(variables)}: Use of Undefined instructions")
                    continue        
            if(i[0] in a):
                    if(len(i[1])!=3):
                        set_of_errors.append(f"Error at line {main_program.index(i)+1+len(variables)}: invalid number of arguments")
                        set_of_mcode.append("FC")
                        continue
                    net_str=op.typea(i,main_program,variables)
                    if(net_str.isnumeric()):
                        set_of_mcode.append(net_str)
                    else:
                        set_of_mcode.append("FC")
                        set_of_errors.append(net_str)
                    program_counter+=1
                    
            elif(i[0] in b and i[1][1] not in dic.reg.keys()):
                    if(len(i[1])!=2):
                        set_of_errors.append(f"Error at line {main_program.index(i)+1+len(variables)}: invalid number of arguments")
                        set_of_mcode.append("FC")
                        continue
                    #edited part
                    temp_num = int(i[1][1][1:])
                    # handling illegal immediate values, only 7 bit binary values are allowed
                    if  temp_num <0 or temp_num>127:
                        set_of_errors.append(f"Error in line {main_program.index(i)+1}: Imm must be a whole number: range (0-127)")
                        net_str="FC"
                        set_of_mcode.append(net_str)
                        continue
                    net_str=op.typeb(i,main_program,variables)
                    if(net_str.isnumeric()):
                        set_of_mcode.append(net_str)
                    else:
                        set_of_mcode.append("FC")
                        set_of_errors.append(net_str)
                    program_counter+=1
                    
                    
            elif(i[0] in c):
                    if(len(i[1])!=2):
                        set_of_errors.append(f"Error at line {main_program.index(i)+1+len(variables)}: invalid number of arguments")
                        set_of_mcode.append("FC")
                        continue
                    net_str=op.typec(i,main_program,variables)
                    if(net_str.isnumeric()):
                        set_of_mcode.append(net_str)
                    else:
                        set_of_mcode.append("FC")
                        set_of_errors.append(net_str)
                    program_counter+=1
                        
                        
            elif(i[0] in d):
                    if(len(i[1])!=2):
                        set_of_errors.append(f"Error at line {main_program.index(i)+1+len(variables)}: invalid number of arguments")
                        set_of_mcode.append("FC")
                        continue
                    # check for valid variable
                    net_str=op.typed(i,variables,main_program,variables)
                    if(net_str.isnumeric()):
                        set_of_mcode.append(net_str)
                    else:
                        set_of_mcode.append("FC")
                        set_of_errors.append(net_str)
                    program_counter+=1

                    
            elif(i[0] in e):
                    if(len(i[1])!=1):
                        set_of_errors.append(f"Error at line {main_program.index(i)+1+len(variables)}: invalid number of arguments")
                        set_of_mcode.append("FC")
                        continue
                    net_str=op.typee(i,labels,main_program,variables)
                    if(net_str.isnumeric()):
                        set_of_mcode.append(net_str)
                    else:
                        set_of_mcode.append("FC")
                        set_of_errors.append(net_str)
                    program_counter+=1
                    
                    
            elif(i[0] in f):
                    net_str=op.typef(i)
                    set_of_mcode.append(net_str)
                    program_counter+=1
                    break
                
            elif(i[0]=="var"):
                set_of_mcode.append("FC")
                set_of_errors.append(f"Error at line {main_program.index(i)+1+len(variables)}: variables must be declared in the begining")
            
            else:  
                    set_of_errors.append("Error: General Syntax Error")
                    continue


    flag=0

    if("hlt"==main_program[-1][0]):
            flag=1
    else:
        for i in main_program:
            if(i[0]=="hlt" and main_program.index(i)!=len(main_program)-1):
                flag=-1
    if(flag==0):
        set_of_errors.append("Error: 'halt' missing program has no end")
        set_of_mcode.append("FC")
    elif(flag==-1):
        set_of_errors.append("Error: 'halt' in the middle of program cannot execute lines after halt")
        set_of_mcode.append("FC")
    flag=0
    for i in set_of_mcode:
        if i=="FC":
            flag=1
            break
    if(flag==0):
        machine_code="\n".join(set_of_mcode)
        #machine_code+="\n"
        fun.write_machine(f"suspend",machine_code)
        print(machine_code)
    else:
        errors="\n".join(set_of_errors)
        #errors+="\n"
        fun.write_machine(f"suspend",errors)
        print(errors)

