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
#lists for opcodes

typeA=["add","sub","mul","and","xor","or"]

typeB=["mov","rs","ls"]

typeC=["div","cmp","mov","not"]

typeD=["ld","st"]

typeE=["jmp","jlt","lgt","je"]

typeF=["hlt"]