import disctionaries as dic
using_op = dic.op_code
using_reg = dic.reg

import functions as op
"""
    op_code={
    "add":"00000",
    "sub":"00001",
    "mul":"00110",
    "div":"00111",
    "xor":"01010",
    "or":"01011",
    "and":"01100",
    "not":"01101",
    "cmp":"01110",
    "mov":["00010","00011"],
    "ld":"00100",
    "st":"00101",
    "rs":"01000",
    "ls":"01001",
    "jmp":"01111",
    "jlt":"11100",
    "jgt":"11101",
    "je":"11111",
    "hlt":"11010",
    "addf": "10000",
    "subf:  "10001",
    "movf": "10010",
}
reg={
    "r0":"000",
    "r1":"001",
    "r2":"010",
    "r3":"011",
    "r4":"100",
    "r5":"101",
    "r6":"110",
    "flags":"111"
}
"""
def typea(ins, machine_c ,variables):
    st = ""
    bb=using_op[ins[0]]
    st += bb
    st += "00"
    if ins[1][0] != "flags" and ins[1][1]!="flags" and ins[1][2]!="flags":
        try:
            st += using_reg[ins[1][0]]
        except:
            st = (f"Error in line {machine_c.index(ins)+1+len(variables)+len(variables)}: invalid register")
            return  st       
        try:
            st += using_reg[ins[1][1]]
        except:
            st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: invalid register")
            return  st 
        try: 
            st += using_reg[ins[1][2]]
            return st
        except: 
            st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: invalid register")
            return  st 
    else:
        st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: entered register is a flag")    
        return  st   
    #st += using_reg[ins[1][0]]
    #st += using_reg[ins[1][1]]
    #st += using_reg[ins[1][2]]
    #return st

def typeb(ins, machine_c, variables):
    st=""
    if(ins[0]=="mov"):
        st += using_op[ins[0]][0]
    else:
        st += using_op[ins[0]]
    st += "0"
    if(op.check_reg(ins[1][0],using_reg)):
        st+=using_reg[ins[1][0]]
        st += op.to_binary(int(ins[1][1][1:]),7)
    else:
        st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: Register Invalid")  
    return st

def typec(ins, machine_c, variables):
    st=""
    if(ins[0]!="mov"):
        st+=using_op[ins[0]]
    else:
        st += using_op[ins[0]][1]
    st+="00000"
    if(op.check_reg(ins[1][0],using_reg) and op.check_reg(ins[1][1],using_reg)):
        st+=using_reg[ins[1][0]]
        st+=using_reg[ins[1][1]]
    else:
        st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: Register Invalid")
    return st

def typed(ins,var_dict, machine_c, variables):
    st = ""
    st += using_op[ins[0]]
    st += "0"
    if(op.check_reg(ins[1][0],using_reg)):
        st+=using_reg[ins[1][0]]
        if(op.check_var([ins[1][1]],var_dict)):        
            st += var_dict[ins[1][1]]
        else:
            st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: Variable {ins[1][1].upper()} not declared")        
    else:
        st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: Register Invalid")
    return st


def typee(ins,label_dict, machine_c,variables):
    st = ""
    st += using_op[ins[0]]
    st += "0000"
    if(op.check_lab([ins[1][0]],label_dict)):        
        st += label_dict[ins[1][0]]
    else:
        st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: Label {ins[1][0]} not found")      
    return st


def typef(ins):
    st = ""
    st += using_op[ins[0]]
    zeroes="0"*11
    st+=zeroes
    return st

#
# Q3. Floating point operations
#
def typea_float(ins,machine_c,variables):
    st = ""
    bb=using_op[ins[0]]
    st += bb
    st += "00"
    if ins[1][0] != "flags" and ins[1][1]!="flags" and ins[1][2]!="flags":
        try:
            st += using_reg[ins[1][0]]
        except:
            st = (f"Error in line {machine_c.index(ins)+1+len(variables)+len(variables)}: invalid register")
            return  st       
        try:
            st += using_reg[ins[1][1]]
        except:
            st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: invalid register")
            return  st 
        try: 
            st += using_reg[ins[1][2]]
            return st
        except: 
            st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: invalid register")
            return  st 
    else:
        st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: entered register is a flag")    
        return  st 
def typeb_float(ins,machine_c,variables):
    st=""
    if(ins[0]=="mov"):
        st += using_op[ins[0]][0]
    else:
        st += using_op[ins[0]]
    if(op.check_reg(ins[1][0],using_reg)):
        st += using_reg[ins[1][0]]
        st +=op.float_to_binary(int(ins[1][1][1:]),8)
    else:
        st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: Register Invalid")  
    return st
#
#
#

#
# Q4. bonus instruction
#
def b_ins1(ins,machine_c,variables):
    st = ""
    bb=using_op[ins[0]]
    st += bb
    st += "00"
    if ins[1][0] != "flags" and ins[1][1]!="flags" and ins[1][2]!="flags":
        try:
            st += using_reg[ins[1][0]]
        except:
            st = (f"Error in line {machine_c.index(ins)+1+len(variables)+len(variables)}: invalid register")
            return  st       
        try:
            st += using_reg[ins[1][1]]
        except:
            st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: invalid register")
            return  st 
        try: 
            st += using_reg[ins[1][2]]
            return st
        except: 
            st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: invalid register")
            return  st 
    else:
        st = (f"Error in line {machine_c.index(ins)+1+len(variables)}: entered register is a flag")    
        return  st 
def b_ins2(ins):
    return
def b_ins3(ins):
    return
def b_ins4(ins):
    return
def b_ins5(ins):
    return
#
#
#

# __________________new______________

def num(n):
    try:
        type(int(n))==int
        return 1
    except:
        return 0