import sys


#get line and map
input_line = int(sys.stdin.readline())
sq_map = []

for i in range(input_line):
    each_line = sys.stdin.readline().split()[0]
    #list comprehension
    list_each_line = [int(each_line[x]) for x in range(len(each_line))]
    sq_map.append(list_each_line)


def dfs(x, y):
    if x <= -1 or x >= input_line or y <= -1 or y >= input_line:
        return False
    if sq_map[x][y] == 1:
        sq_map[x][y] = 0 #change to 0 as visited.
        block.append(1) #add block count
        #call Recursion function.
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

block =[]
total_block = 0
block_list = []
for i in range(input_line):
    for j in range(input_line):
        a = dfs(i, j)
        #print(f'{i},{j} = {a}')
        if a == True:
            total_block += 1
            #print(cnt)
            block_list.append(len(block))
            block = []

print(total_block)
#print(block_list)
block_list.sort()
for i in block_list:
    print(i)