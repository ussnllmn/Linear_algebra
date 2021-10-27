import numpy as np

F1 = int(input('Enter total orchid in farm 1: '))
F2 = int(input('Enter total orchid in farm 2: '))
DA = int(input('Enter total need of dealer A: '))
DB = int(input('Enter total need of dealer B: '))

r = np.array([
    [1,1,0,0,F1],
    [0,0,1,1,F2],
    [1,0,1,0,DA],
    [0,1,0,1,DB], 
    [220,300,400,180,10640]
])

r[2] = (-1*r[0]+r[2])
print ('\n1. r[2] = (-1*r[0]+r[2])\nResult =',r[2],'\n',r)

r[4] = (-220*r[0]+r[4])
print ('\n2. r[4] = (-220*r[0]+r[4])\nResult =',r[4],'\n',r)

r[[1, 3]] = r[[3, 1]]
print ('\n3. r[[1, 3]] = r[[3, 1]]\nResult = Swap r1 and r3','\n',r)

r[2] = (r[1]+r[2])
print ('\n4. r[2] = (r[1]+r[2])\nResult =',r[2],'\n',r)

r[4] = (-80*r[1]+r[4])
print ('\n5. r[4] = (-80*r[1]+r[4])\nResult =',r[4],'\n',r)

r[3] = (-1*r[2]+r[3])
print ('\n6. r[3] = (-1*r[2]+r[3])\nResult =',r[3],'\n',r)

r[4] = (-400*r[2]+r[4])
print ('\n7. r[4] = (-400*r[2]+r[4])\nResult =',r[4],'\n',r)

r[[3, 4]] = r[[4, 3]]
print ('\n8. r[[3, 4]] = r[[4, 3]]\nResult = Swap r3 and r4','\n',r)

r[3] = (-1/300*r[3])
print ('\n9. r[3] = (-1/300*r[3])\nResult =',r[3],'\n',r)

r[2] = (-1*r[3]+r[2])
print ('\n10. r[2] = (-1*r[3]+r[2])\nResult =',r[2],'\n',r)

r[1] = (-1*r[3]+r[1])
print ('\n11. r[1] = (-1*r[3]+r[1])\nResult =',r[1],'\n',r)

r[0] = (-1*r[1]+r[0])
print ('\n12. r[0] = (-1*r[1]+r[0])\nResult =',r[0],'\n',r,'\n')

print ('Farm 1 has a total of',F1,'orchids to send.')
print ('Send to dealer A amount',r[0][4],'orchids.')
print ('Send to dealer B amount',r[1][4],'orchids.\n')

print ('Farm 2 has a total of',F2,'orchids to send.')
print ('Send to dealer A amount',r[2][4],'orchids.')
print ('Send to dealer B amount',r[3][4],'orchids.\n')

print ('Dealer A gets total orchid is',r[0][4]+r[2][4])
print ('Dealer B gets total orchid is',r[1][4]+r[3][4],'\n')