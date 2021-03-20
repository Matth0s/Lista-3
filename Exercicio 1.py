'''
Esse programa imprime a tabela ASCII
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''

print("...................................................................... ")
print("Esse programa mostra a tabela ASCII com inicio e fim escolhidos por")
print("você\n")
print("Para iniciar, digite tabela(x,y,z), onde x é o inicio da tabela, y é")
print("o fim da tabela e z é o numero de linhas que cada pagina da tabela ")
print("vai ter")
print("...................................................................... \n")

def tabela(x = 32,y = 127, z = 25):
    if x > y:
        ini = y
        fim = x
    else:
        ini = x
        fim = y

    if z <=0:
        z=25

    if ini < 32:
        ini = 32

    if fim < 32:
        fim = 32

    if ini > 127:
        ini = 127

    if fim > 127:
        fim = 127

    print("+","~"*9,"+","~"*3,"+","~"*3,"+","~"*3,"+","~"*3,"+")
    print("|  Binário  | Oct | Hex | Dec | Chr |")
    print("+","~"*9,"+","~"*3,"+","~"*3,"+","~"*3,"+","~"*3,"+")
    for i in range(ini,fim+1):
        bina = "{0:08b}".format(i)
        print("| {1} {2} | {0:^3o} | {0:^3X} | {0:^3d} |  {0:^c}  |".format(i,bina[:4],bina[4:]))
        if (i-ini+1)%z==0 and (i-fim)!=0:
            print("+","~"*9,"+","~"*3,"+","~"*3,"+","~"*3,"+","~"*3,"+")
            print("")
            print("+","~"*9,"+","~"*3,"+","~"*3,"+","~"*3,"+","~"*3,"+")
            print("|  Binário  | Oct | Hex | Dec | Chr |")
            print("+","~"*9,"+","~"*3,"+","~"*3,"+","~"*3,"+","~"*3,"+")
    print("+","~"*9,"+","~"*3,"+","~"*3,"+","~"*3,"+","~"*3,"+")










        

