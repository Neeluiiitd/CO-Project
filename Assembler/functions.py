# creates a filtered string eliminating blanklines
def blank_factors(string):
    if("\n\n" in string):
        k=string.split("\n\n")
        k="\n".join(k)
        string=k
    if(string[:1]=="\n"):
        string=string[1:]
    return string

# creates a dictionary with opcodes and there corresponding opeartions for initial stage 
def extract(filename):
    f=open(filename,"rt")
    set_string=f.read()
    f.close()
    net_matrix=set_string.split("\n\n\n")
    return net_matrix

def ins_return(filename):
    n_string=extract(filename)
    master_record=[]
    for set_string in n_string:
        intruction_set=[]
        if(set_string==""):
            emp=[]
            return emp
        set_string=blank_factors(set_string)
        set_string=set_string.lower()
        for i in set_string.split("\n"):
            temp_list=i.split()
            intruction_set.append([temp_list[0],temp_list[1:]])
        master_record.append(intruction_set)
    return master_record

# creates a 7-bit binary string 
def to_binary(n, m):
    if n == 0:
        binary ="0"
        while(len(binary)!=m):
            binary="0"+binary
        return binary
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    while(len(binary)!=m):
        binary="0"+binary
    return binary
#to decimal
def binaryToDecimal(n):
    num = n
    dec_value = 0
     
    # Initializing base
    # value to 1, i.e 2 ^ 0
    base = 1
     
    temp = num
    while(temp):
        last_digit = temp % 10
        temp = int(temp / 10)
         
        dec_value += last_digit * base
        base = base * 2
    return dec_value
# create a dictionary
def prg_mem(dict_name):
    count=len(dict_name)
    mem_reserve=[]
    for i in range(count):
        mem_id=to_binary(i,7)
        mem_reserve.append([mem_id,""])
    return mem_reserve
f=ins_return("Tech.txt")
g=prg_mem(f)
#creates a dictianary of labels
def ad_dict(prg_dict,machine_dict):
    mac=[i[0] for i in prg_dict]
    ad=[i[0] for i in machine_dict]
    count=len(mac)
    new_dict={}
    for i in range(count):
        if(":" in mac[i]):
            new_dict[mac[i][:-1]]=ad[i]
    return new_dict

#creates a dictionary of variables
def cr_var(prg_dict,machine_dict):
    k=[]
    for i in prg_dict:
        if(i[0]=="var"):
            k.append(i)
        else:
            break
    v=[i[0] for i in machine_dict]
    count=len(k)
    v=v[-count:]
    n_dict={}
    for i in range(count):
        n_dict[k[i][1][0]]=v[i]
    return n_dict

#removes labels
def rm_label(prg_dict):
    count=0
    for i in prg_dict:
        if(i[0]=="var"):
            count+=1
        else:
            break
    prg_ls=prg_dict[count:]
    count=len(prg_ls)
    for i in range(count):
        if(":" in prg_ls[i][0]):
            prg_ls[i][0]=prg_ls[i][1][0]
            prg_ls[i][1]=prg_ls[i][1][1:]
    return prg_ls


# funtion to check variables
def check_var(value,var):
    for i in var.keys():
        if value[0]==i:
            return True
    return False

# funtion to check labels
def check_lab(labels,lab):
    for i in lab.keys():
        if labels[0]==i:
            return True
    return False

# funtion to check registers
def check_reg(reg,regs):
    if(reg=="flags"):
        return False
    for i in regs.keys():
        if i == reg:
            return True
    return False

# fucntion to find flag and non flag regs

def check_flag(reg,regs):
    if(reg=="flags"):
        return -1
    for i in regs.keys():
        if i == reg:
            return 1
    return 0
# fucntion to check if a halt fucntion exists
def check_halt(main_program):
    for i in main_program:
        if i[0]=="hlt":
            return True
    return False
# function to write machine code in a text file
def write_machine(filename,machine_code):
    f=open(filename,"at")
    f.write(machine_code)
    f.close()