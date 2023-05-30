f=open("input",'r')
a=f.readlines()
# print(a)
machine_code=[]
# __________________________IMPORT________________________
import Dictionaries as dic
import Functions as func
for i in a:
    machine_code.append(i[:-1])

# for i in machine_code:
#     print(i)
for i in machine_code:
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


# print(dic.reg)