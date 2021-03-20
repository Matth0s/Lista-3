'''
Esse programa cria um arquivo com a frequencia das palavras de
arquivos txt
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''
print("...................................................................... ")
print("Aqui tu pode criar um arquivo que mostre a frequência das palavras")
print("contidas em arquivos txt\n")
print("A) digite 1 se você quiser a lista em ordem lexicográfica")
print("B) digite 2 se vocÊ quiser a lista em ordem de frequência do mais")
print("frequente ao menos frequênte")
print("...................................................................... \n")

# analiza o codigo de baixo pra cima, vai fazer sentido assim
import os

def escrita_lex(y):# parada alfabetica
    unics = []
    for i in y:
        if i not in unics:
            unics.append(i)
    
    escrita = open('Frequencia.txt','w')# só pra ficar mais bonitinho também
    escrita.writelines("+~~~~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~+\n")
    escrita.writelines("|       Palavras       |   Frequência   |\n")
    escrita.writelines("+~~~~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~+\n")
    t = sorted(unics)
    for i in t:
        f = y.count(i)
        escrita.writelines("| {0:^20} | {1:^14} |\n".format(i,f))
        escrita.writelines("+----------------------+----------------+\n")
    escrita.close()
    return

def escrita_freq(y):# parada da frequência
    unics = []
    freq=[]
    plv_ord =[]

    for i in y:# cria a lista sem repetir palavras
        if i not in unics:
            unics.append(i)
    t = sorted(unics)

    for i in t:# vai me dizer as frequências dentro do bagulho la
        ind = y.count(i)
        if ind not in freq:
            freq.append(ind)
        else:
            pass
    freq_ord = sorted(freq, reverse=True)
    
    for i in freq_ord:# bota na lista as palavras em ordem de frequência
        for j in t:
            if i == y.count(j):
                plv_ord.append(j)
    
    escrita = open('Frequencia.txt','w')# só pra ficar mais bonitinho também
    escrita.writelines("+~~~~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~+\n")
    escrita.writelines("|       Palavras       |   Frequência   |\n")
    escrita.writelines("+~~~~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~+\n")
    
    for i in plv_ord:# escreve no arquivo
        w = y.count(i)
        escrita.writelines("| {0:^20} | {1:^14} |\n".format(i,w))
        escrita.writelines("+----------------------+----------------+\n")
    escrita.close()
    return

def palavras(x):
    arq = os.listdir(".")# abre o diretorio
    txts = []
    plvrs = []
    for i in arq:# pega só os txt
        if i[-4:]=='.txt':
            txts.append(i)
        else:
            pass

    for i in txts:# lê todos os txt e taca as palavras encontradas em uma lista
        abrir = open(i,'r')
        ler = abrir.read()
        sep = ler.split()
        
        for i in sep:# tira tudo que eu não considero pertinente e bota na lista de palavras
            if len(i)>2:
                c1=i.lower()
                c2=c1.replace(",","")
                c3=c2.replace('"',"")
                c4=c3.replace(".","")
                c5=c4.replace("(","")
                c6=c5.replace(")","")
                c7=c6.replace(":","")
                c8=c7.replace(";","")
                plvrs.append(c8)
            else:
                pass

    
    
    if x == 1:# manda pra parada alfabetica ou pra parada da frequência
        escrita_lex(plvrs)
        print("Arquivo Criado")

    else: 
        escrita_freq(plvrs)
        print("Arquivo Criado")



ordem = int(input("- "))# só pra ver em que ordem o usuario quer mesmo
while ordem != 2 and ordem != 1:
    print("Éssa opção ai nem vale filho, tenta de novo\n")
    ordem = int(input("- "))
    
if ordem == 1:
    palavras(1)
else:
    palavras(2)


        
        
