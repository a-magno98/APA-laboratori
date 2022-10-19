import numpy as np
import random as rd

def update_mat(proc,n,a):
    mat = np.empty((n, 0)).tolist()
    for i in range(0,a):
        mat[i].append(proc[i])
    for i in range(a, n):
        mat[i].append(rd.randint(0,1))                      
    return mat

def send_random_value(mat,a,n):
  value = rd.randint(0,1)
  for j in range(a, n):
    for i in range(0, n):
        if(j != i):
            mat[i].append(value)

def send_value(mat,a,n):
  for j in range(0,a):
    for i in range(0, n):
        if(j != i):
            mat[i].append(mat[j][0])
  send_random_value(mat,a,n)
    
def calculate_maj(r,a):
    maj = np.empty((a, 0)).tolist()
    for i in range(0,a):
       if r[i].count(0)>r[i].count(1):
            maj[i].append(0)
            maj[i].append(r[i].count(0))
       else:
            maj[i].append(1)
            maj[i].append(r[i].count(1))
    return maj

def calculate_tally(maj,a):
    tally = []
    for i in range(0,a):
        tally.append(maj[i][1])
    return tally

def check_tally(tally, t, maj, moneta,a):
    proc = []
    for i in range(0,a):
        if tally[i] >= 2*t+1:
            proc.append(maj[i][0])
        elif moneta == "testa":
            proc.append(1)
        else:
            proc.append(0)
    return proc

def check_process(proc,a):
    first = proc[0]
    for i in range(0,a):
        if(first != proc[i]):
            return 0
    return 1
            
#implementazione algo
def algorithm(mat,a,n,t):
    round = 1
    while(1):
        #lancio della moneta
        moneta = rd.choice(["testa","croce"])
        #trasmetti b(i) agli altri n-1 processi e spedizione valori degli n-1 processi
        ##i valori vengono salvati come: [[val1,ric1,ric2,ric3..], [val2,ric1,ric2..]..]
        send_value(mat,a,n)
        #ricevi i valori spediti dagli altri n-1 processi + b(i) incluso
        r = mat.copy()
        #valutazione maggioritario
        maj = calculate_maj(r,a)
        ##al maj ho aggiunto anche il tally in modo da estrarlo dopo
        ##es maj = [[num_maj, tally]]
        #numerosità di maj
        tally = calculate_tally(maj,a)
        #check tally >= 2t + 1 e ritorna nuova matrice con solo i processi
        proc = check_tally(tally, t, maj, moneta, a)
        #controllo se tutti i processi hanno lo stesso valore, in tal caso
        ##hanno raggiunto il consenso
        if(check_process(proc,a)):
            print("Consenso raggiunto in round: ", round)
            print(proc)
            break
        #aggiorno la matrice con i nuovi valori dei processi
        mat = update_mat(proc,n,a)
        round = round + 1

def fill_matrix(mat,a,n,v0):
    for i in range(0,a):
        mat[i].append(v0)

    for i in range(a,n):
        mat[i].append(0)
        
def fill_matrix_2(mat,a,n):
    for i in range(0,n):
        mat[i].append(rd.randint(0,1))
    
def main():
    #processi totali
    n = 31
    #traditori
    t = 10
    #affidabili
    a = n-t
    #v0 inziale (esercizio 1)
    #v0=1
    #matrice generale
    mat = np.empty((n, 0)).tolist()
    
    #per esercizio 1
    #fill_matrix(mat,a,n,v0)
    #per esercizio 2
    fill_matrix_2(mat,a,n)
    """
    valori dei processi nella matrice sono
    inseriti come [[val1],[val2]..]
    """
    for i in range(0,100):
        algorithm(mat,a,n,t)
    
main()