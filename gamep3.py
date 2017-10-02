from random import *

def game(p,text):
	count = 0

	for v in matrix:
		for i,j in enumerate(v):
			if p == j:
				v[i] = text
				count = count + 1 
	
	for v in n:
		if int(p) == v:
			n.remove(int(p))

	print()
	for v in matrix:
		for z in v:
			if z!=player1[0] and z != player2[0]:
				print('-',end=" ")
			else:
				print(z,end=" ")
		print()
	print()
	return count



totc1 = totc2 = 0
matrix = []
n = [1,2,3,4,5,6]

print("----------------------------")
print("\tCLEAN SWEEPER\t")
print("----------------------------")
player1 = input("Enter Player A name: ")
player2 = input("Enter Player B name: ")
print()

for i in range(10):
    l = []
    for j in range(10):
        l.append(str(randint(1,6)))
    matrix.append(l)

for v in matrix:
		for z in v:
			print('-',end=" ")
		print()

print("Enter any number between 1 & 6")
print("Remaining : ",n)

for t in range(3):
    print(player1+"'s turn:")
    p1 = input()
    c1 = game(p1,player1[0])
    print(player1+"'s score:")
    print("=> Level",t+1," : ",c1)
    totc1+=c1
    print("=> Current Total : ",totc1)
    print("Remaining : ",n)

    print(player2+"'s turn:")
    p2 = input()
    c2 = game(p2,player2[0])
    print(player2+"'s score:")
    print("=> Level",t+1," : ",c2)
    totc2+=c2
    print("=> Current Total : ",totc2)
    print("Remaining : ",n)
print()
print("Final Scores :")
print(player1+" : ",totc1)
print(player2+" : ",totc2)
if totc1 > totc2:
	print(player1+" wins")
elif totc1 < totc2:
	print(player2+" wins")
else:
	print("= = =It was a Tie! = = =")





