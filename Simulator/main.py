import Components as cpu
import sys

# Create a list to store the input lines

# Loop over the input lines
arg=[]
while True:
    try:
        stdin=input()
        arg.append(stdin)
    except:
         break
#ls=sys.stdin.

ee=cpu.EE(arg)
pc=ee.pc
fr=ee.regs
mem=ee.memory
mem.store_the_program()

while(True):
    instruction=mem.memory[pc.address]
    if(instruction[:5]=="11010"):
        break
    ee.execute(instruction)
    print(pc,end="\t")
    print(fr,end="\n")
    pc.increment()
print(mem)