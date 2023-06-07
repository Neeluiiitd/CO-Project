import Components as cpu
import sys

# Create a list to store the input lines

# Loop over the input lines
arg=[]
while True:
    try:
        g=input()
    except:
        break
    arg.append(g)
#ls=sys.stdin.

ee=cpu.EE(arg)
pc=ee.pc
fr=ee.regs
mem=ee.memory
mem.store_the_program()

while(True):
    instruction=mem.memory[pc.address]
    if(instruction[:5]=="11010"):
        print(pc,end="        ")
        print(fr,end="\n")
        break
    ee.execute(instruction)
    print(pc,end="        ")
    print(fr,end="\n")
    pc.increment()
print(mem)