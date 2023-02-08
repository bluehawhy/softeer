
import sys

M, N, K = map(int,sys.stdin.readline().split())
secret_key = sys.stdin.readline()
user_input = sys.stdin.readline()



def case1():
    user_input_sp = user_input.split(secret_key)
    print(user_input_sp)
    print(len(user_input_sp))
    if len(user_input_sp) > 1:
        print('secret')
    else:
        print('normal')


def case2():
    list_secret_key = secret_key.split()
    list_user_input = user_input.split()
    #print(list_secret_key)
    cnt = 0
    find_key = 0
    for i in list_user_input:
        #check
        if i == list_secret_key[0]:
            print(list_user_input[cnt:cnt+M])
            if list_user_input[cnt:cnt+M] == list_secret_key:
                print('secret')
                find_key = find_key + 1
                break
        cnt = cnt + 1
    if find_key == 0:
        print('normal')
        
case2()