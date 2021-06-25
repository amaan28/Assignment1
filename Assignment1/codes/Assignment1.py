import random
n = 3000000    #Number of times the experiment is done.
Xctr = [0,0,0,0]                                     #Counter Variable that counts the number of times X attains each value from the set {0,1,2,3}
for j in range(n):                                   #j counts how many times the experiment is obtained, also, experiment number. 
  r = 0
  for i in range(3):                                 #Throw number in that experiment
    X = random.randint(1,6)                         #Number on dice 1
    Y = random.randint(1,6)                         #Number on dice 2
    if X==Y:
      r+= 1
  Xctr[r] += 1
print("SIMULATION\n")
for i in range(4):
  print(f"\n\t\tPr(Z={i}) = {Xctr[i]/n} ")
print("\nTHEORY\n")
print(f"\n\t\tPr(Z=0) = 0.5787")
print(f"\n\t\tPr(Z=1) = 0.3469")
print(f"\n\t\tPr(Z=2) = 0.0694")
print(f"\n\t\tPr(Z=3) = 0.0046")
