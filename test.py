

mapping = [[0,1,0,1],[0,1,0,1],[1,1,0,1],[0,1,0,1]]

for m in mapping:
    print(m)

def check(x,y):
    if mapping[x][y] == 1:
         mapping[x][y] = 0


for i in range(2):
    for j in range(2):
        check(i,j)

print('==================')
for m in mapping:
    print(m)