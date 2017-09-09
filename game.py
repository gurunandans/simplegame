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

	print "\n"
	for v in matrix:
		for z in v:
			if z!='A' and z != 'B':
				print '-',
			else:
				print z,
		print "\r"
	print "\n"
	return count



totc1 = 0
totc2 = 0
matrix = []
n = [1,2,3,4,5,6]

print "----------------------------"
print "\tCLEAN SWEEPER\t"
print "----------------------------\n"
print "Enter Player A name: "
player1 = raw_input()
print "Enter Player B name: "
player2 = raw_input()
print "\n"

for i in range(10):
    l = []
    for j in range(10):
        l.append(str(randint(1,6)))
    matrix.append(l)

for v in matrix:
		for z in v:
			print '-',
		print "\r"

print "Enter any number between 1 & 6"
print "Remaining : ",n

for t in range(3):
    print "\n"+player1+"'s turn:"
    p1 = raw_input()
    c1 = game(str(p1),'A')
    print player1+"'s score:"
    print "=> Level %d : "%(t+1),c1
    totc1+=c1
    print "=> Current Total : ",totc1
    print "\nRemaining : ",n

    print "\n"+player2+"'s turn:"
    p2 = raw_input()
    c2 = game(str(p2),'B')
    print player2+"'s score:"
    print "=> Level %d : "%(t+1),c2
    totc2+=c2
    print "=> Current Total : ",totc2
    print "\nRemaining : ",n
print "\n"
print "Final Scores :"
print player1+" : ",totc1
print player2+" : ",totc2
if totc1 > totc2:
	print player1+" wins"
elif totc1 < totc2:
	print player2+" wins"
else:
	print "= = =It was a Tie! = = ="





