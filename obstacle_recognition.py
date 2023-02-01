

input_samle=['7',
'1110111',
'0110101',
'0110101',
'0000100',
'0110000',
'0111110',
'0110000']



import sys


#get line and map
#input_line = int(sys.stdin.readline())
sq_map = []

input_line = int(input_samle[0])

for i in range(input_line):
    #each_line = sys.stdin.readline().split()[0]
    each_line=input_samle[i+1]
    #list comprehension
    list_each_line = [each_line[x] for x in range(len(each_line))]
    sq_map.append(list_each_line)


def show_map():
    for s_m in sq_map:
        print(s_m)


cnt =[]
def dfs(x, y):
    if x <= -1 or x >= input_line or y <= -1 or y >= input_line:
        return False
    if sq_map[x][y] == 1:
        # 해당 노드 방문 처리
        sq_map[x][y] = 0
        # 장애물의 개수 체크
        cnt.append(1)
        
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

show_map()
dfs(0,0)
print( '===================================' )
show_map()