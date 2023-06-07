import Components as cpu
import sys

# Create a list to store the input lines
lines = []

# Loop over the input lines
for line in sys.stdin:
    if(line=="\n"):
        break
    line = line.strip()
    lines.append(line)

ee=cpu.EE(lines)
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