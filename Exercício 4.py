'''
Esse programa conta as linhas e colunas dos arquivos csv
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''
print("...................................................................... ")
print("Aqui tu pode contar as linhas e as colunas de um arquivo csv")
print("Para iniciar digita numero('x') onde o x é o nome do seu arquivo csv")
print("...................................................................... \n")

import csv

def linhas(z):
    
    ficheiro = open(z, 'r')
    ler = ficheiro.read()
    linhas = ler.split()
    n_lin = len(linhas)
    return n_lin

def colunas(y):
    
    ficheiro = open(y, 'r')
    ler = ficheiro.read()
    linhas = ler.split()
    linha1 = linhas[0]
    colunas = linha1.split(',')
    n_col = len(colunas)
    return n_col



def numero(x):
    w1 = linhas(x)
    w2 = colunas(x)
    print("......................................................................")
    print("O arquivo {} tem {} linhas e {} colunas".format(x,w1,w2))
    print("......................................................................")



