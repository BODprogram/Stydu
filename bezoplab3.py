
def text_to_char(filename):
    massiv_char=[]
    with open(filename, encoding="utf-8") as f:
        while True:
            liter = f.read(1)
            #print(type(liter))
            massiv_char.append((liter))
            #print(liter)
            if not liter:
                print
                "End of file"
                break
    massiv_char.pop(0) # удаляет \ufeff от кодиоровки
    massiv_char.pop(len(massiv_char)-1) # удаляет ''
    return massiv_char


def hash_easy(massiv_char):
    hash_otv=0
    dop_liter1='a'
    dop_liter2='b'
    for i in range(0, len(massiv_char)):
        num1=ord(massiv_char[i])
        dop_ord_liter1=(ord(dop_liter1))
        dop_ord_liter2=(ord(dop_liter2))
        num2=num1*num1*i*i*dop_ord_liter1*dop_ord_liter2+num1
        dop_liter1=massiv_char[i]
        if i+2<(len(massiv_char)):
            dop_liter2 = massiv_char[i+2]
        hash_otv = hash_otv+num2

#54959cb88270ddcde3a5c864242fe792b
#54959a48c1f9d2705cc34c6c214fe792b
    return hash_otv

def hash_hard(massiv_char):
    hash_otv = hash_easy(massiv_char)
    while len(str(hex(hash_otv)))<42:
        hash_otv=hash_otv*hash_otv

    hash_otv=str(hex(hash_otv))
    print(str(hash_otv))
    hash_otv=(str(hash_otv)[8:40])


    return hash_otv

#print('Текст1: ',text_to_char('1.txt'))
#print('Хэш1: ',hash_easy(text_to_char('1.txt')))
#print('Хэш2: ',hash_hard(text_to_char('1.txt')))
print('Текст2: ',text_to_char('2.txt'))
print('Хэш1: ',hash_easy(text_to_char('2.txt')))
print('Хэш2: ',hash_hard(text_to_char('2.txt')))
print('Текст3: ',text_to_char('3.txt'))
print('Хэш1: ',hash_easy(text_to_char('3.txt')))
print('Хэш2: ',hash_hard(text_to_char('3.txt')))
#print('Текст4: ',text_to_char('4.txt'))
#print('Хэш1: ',hash_easy(text_to_char('4.txt')))
#print('Хэш2: ',hash_hard(text_to_char('4.txt')))
