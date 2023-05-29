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