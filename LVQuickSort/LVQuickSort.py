import random
import matplotlib.pyplot as plt
import math

#generazione casuale 10000 numeri
"""
l = random.sample(range(10000), 10000)
with open('numbers.txt', 'w') as f:
    for item in l:
        f.write("%s\n" % item)
"""

#confronti
comparisons = 0

def Partition(A,left,right):
    global comparisons
    rindex = random.randrange(left,right+1)
    A[rindex],A[right] = A[right],A[rindex]
    pivot = A[right]
    i = left-1
    j = left
    while j < right:
        if A[j] <= pivot:
            i+=1
            A[i],A[j]=A[j],A[i]
        j+=1
        comparisons+=1
    A[i+1],A[right]=A[right],A[i+1]
    return i+1

def LVQuickSort(A,left,right):
    if left < right:
        q = Partition(A,left,right)
        LVQuickSort(A,left,q-1)
        LVQuickSort(A,q+1,right)
        
def main():

  global comparisons
  #lista confronti ad ogni iterazione
  list_of_comparisons = []
  #totale di tutti i confronti effettuati
  totale_comparisons = 0
  #numeri run di iterazioni
  R = 10000
  #dimensioni lunghezza sequenza
  n = 10000
  """
  for i in range(0,R):
      A = []
      f=open('numbers.txt',"r")
      for line in f:
        A.append(int(line.strip('\n')))
      left = 0
      right = len(A)-1
      LVQuickSort(A,left,right)
      list_of_comparisons.append(comparisons)
      totale_compparisons+=comparisons
      comparisons = 0

 #salvo i risultati in un file
  with open('comparisons.txt', 'w') as f:
    for item in list_of_comparisons:
        f.write("%s\n" % item)
  with open('totale_comparisons.txt', 'w') as f:
      f.write("%s\n" % totale_comparisons)

  """    
 #se ho già i risultati li apro
  with open('comparisons.txt',"r") as f:
      for line in f:
          list_of_comparisons.append(int(line.strip('\n')))
  
  with open('totale_comparisons.txt') as f:
    totale_comparisons = int(f.readline())
  
  #stampa la figura
  plt.figure(figsize=(16,8))
  plt.hist(list_of_comparisons, bins=int(math.log2(totale_comparisons)+1))
  
  #stima di C
  estimate_C = 1/R*totale_comparisons / (n*math.log(n))
  print("Stima di C: ", estimate_C)
main()