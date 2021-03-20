'''
Esse programa imprime a tabela com os codigos Unicodes
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''

print("...................................................................... ")
print("Esse programa mostra a tabela com os codigos Unicodes inicio e fim ")
print("escolhidos por você\n")
print("Para iniciar, digite tabela(x,y,z), onde x é o inicio da tabela, y é")
print("o fim da tabela e z é o numero de linhas que cada pagina da tabela")
print("vai ter")
print("...................................................................... \n")


def tabela(x = 32,y = 10495, z = 25):
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

    if ini > 10495:
        ini = 10495

    if fim > 10495:
        fim = 10495


    print("+","~"*15,"+","~"*5,"+","~"*5,"+","~"*5,"+","~"*3,"+")
    print("|     Binário     |  Oct  |  Hex  |  Dec  | Chr |")
    print("+","~"*15,"+","~"*5,"+","~"*5,"+","~"*5,"+","~"*3,"+")
    for i in range(ini,fim+1):
        bina = "{0:014b}".format(i)
        print("| {1} {2} | {0:^5o} | {0:^5X} | {0:^5d} |  {0:^c}  |".format(i,bina[:7],bina[7:]))
        if (i-ini+1)%z==0 and (i-fim)!=0:
            print("+","~"*15,"+","~"*5,"+","~"*5,"+","~"*5,"+","~"*3,"+")
            print("")
            print("+","~"*15,"+","~"*5,"+","~"*5,"+","~"*5,"+","~"*3,"+")
            print("|     Binário     |  Oct  |  Hex  |  Dec  | Chr |")
            print("+","~"*15,"+","~"*5,"+","~"*5,"+","~"*5,"+","~"*3,"+")
    print("+","~"*15,"+","~"*5,"+","~"*5,"+","~"*5,"+","~"*3,"+")










        

