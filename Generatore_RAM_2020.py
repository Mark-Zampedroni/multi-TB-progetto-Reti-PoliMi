import random

# Generatore di test per l'anno 2019/2020 - per gli anni successivi andra' modificato in funzione delle specifiche di progetto

def create_wz(): # Inizializza gli indirizzi salvati nella RAM - nel contesto 2019/2020 si chiamano WZ 
    new_wz = []
    k = 0
    while k < 8:
        d = 0
        wz = random.randint(0,124)
        for elem in new_wz:
            if((elem <= wz <= elem+3) or (wz <= elem <= wz+3)):
                d = 1
        if not d:
            new_wz.append(wz)
            k = k + 1
    return new_wz

def create_addr_and_cod(wz_list): # Crea la coppia (input,output atteso)
    addr_da_cod = random.randint(0,127)
    addr_codificato = "0000"
    k = 0
    for wz in wz_list:
        if(wz <= addr_da_cod <= wz+3):
            addr_codificato = list(addr_codificato)
            addr_codificato[-((addr_da_cod - wz) + 1)] = "1"
            addr_codificato = "".join(addr_codificato)
            addr_codificato = "1" + str(bin(k)[2:].zfill(3)) + addr_codificato
        k = k + 1
    if addr_codificato == "0000":
        return addr_da_cod, addr_da_cod
    else:
        return addr_da_cod, int(addr_codificato, 2)
            

test = []
for i in range(1,11): #Genera 30 test (10*3)
    # Test start singolo
    new_wz = create_wz()
    addr_da_cod, addr_codificato = create_addr_and_cod(new_wz)
    addr_da_cod2, addr_codificato2 = create_addr_and_cod(new_wz)
    new_wz.append(addr_da_cod)
    new_wz.append(0)
    new_wz.append(addr_codificato)
    test.append(new_wz)
    
    # Test secondo start
    new_wz2 = new_wz[:]
    new_wz2[8] = addr_da_cod2
    new_wz2[10] = addr_codificato2
    test.append(new_wz2)
    
    # Test reset sincrono
    new_wz = create_wz()
    addr_da_cod, addr_codificato = create_addr_and_cod(new_wz)
    new_test = new_wz
    new_test.append(addr_da_cod)
    new_test.append(0)
    new_test.append(addr_codificato)
    test.append(new_test)
        
with open('ram_content.txt','w') as w:
    for each_test in test:
        for elem in each_test:
            w.write(str(elem)+"\n")

with open('valori_test.txt','w') as w:
    num = 1
    for each_test in test:
        w.write(str(num) + ") RAM: " + str(each_test[:-2]) + " - output atteso: " + str(each_test[-1]) +"\n")
        num = num + 1
            
