import gate_impl #importing gate_impl


def bit_adder(a, b): #assinging  variables
    a = a[::-1]
    b = b[::-1]
    result = []
    last_carry = 0
    for i in range(0, 8): #for loop
        r1 = gate_impl.and_gate(a[i], b[i]) 
        r2 = gate_impl.xor_gate(a[i], b[i]) 
        r3 = gate_impl.and_gate(r2, last_carry)
        r4 = gate_impl.nor_gate(r1, r3)
        carry = gate_impl.not_gate(r4)
        r6 = gate_impl.nand_gate(r2, last_carry)
        r7 = gate_impl.or_gate(r2, last_carry)
        sum_bit = gate_impl.and_gate(r6, r7)
        result.insert(0, sum_bit)
        last_carry = carry
    return result
