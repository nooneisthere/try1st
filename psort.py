#coding=utf-8
from pprint import pprint
import sys, datetime

sys.setdefaultencoding('utf-8')

print 0;
sys.exit(0);
#sys.exit('bye!');
#汉诺塔 递归减化成移动二个积木的过程，N和N-1个
def hanoi(n, mfrom, mhelp, mto):
    if n > 1:
        #把所有上面的N-1个移动到中间help柱子上
        hanoi(n - 1, mfrom, mto, mhelp)

        #把下面最大的N移动到目标柱子上
    print('move ',n, ' from ', mfrom, '-->', mto)
        #把辅助盘上的N-1个移动到目标柱子上
    if n > 1:
        hanoi(n - 1, mhelp, mfrom, mto)
# 调用
#hanoi(4, 'A', 'B', 'C')



#快速排序 - 递归
#是每次要找到中轴值，然后左右两边再进行快排。
#这个中轴值，实际和每个数字都比较过，所以每次中轴的位置确定下来不不需要再排，
#对剩下的子列进行排序


def sort_quick(int_array,low,high):
    start = low;
    end = high;
    while(high>low):
        temp = int_array[low]

        while(high>low):
            high -= 1
            if(int_array[high] < int_array[low]):
                int_array[low] = int_array[high]
                break

        while(high>low):
            low += 1
            if (temp < int_array[low]):
                int_array[high] = int_array[low]
                break
        #要注意如果temp是最大的，会出现找不到插入位置的情况
        #所以这个temp插入赋值放在循环条件外确保插入
        int_array[low] = temp

        print(int_array);

    print('mid',high,start,end);
    if (end - low > 1):
        sort_quick(int_array,low+1,end)


    if (low - start > 1):
        sort_quick(int_array,start,low)




#print(sort_quick([0,1,8,5,6,2,1,7,0],0,9))


#希尔排序
def sort_shell(int_array):
    j=0
    temp=0
    inc=len(int_array) // 2
    while (inc>0):
        i=inc
        while (i<len(int_array)):
            temp = int_array[i]
            j=i
            while j>=inc :
                if temp > int_array[j - inc]:
                    int_array[j] = int_array[j - inc]
                else:
                    break

                int_array[j] = temp
                j -= inc
            i+=1
        inc = inc // 2

        print(int_array)


#sort_shell([0,1,8,5,6,2,1,7,9,0])


def shell_sort(array):
    gap = len(array)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(array)):
            for j in range(i % gap, i, gap):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
    return array


#print(shell_sort([0,1,8,5,6,2,1,7,9,0]))


def insert_sort(array):

    for i in range(1,len(array)):
        temp = array[i]
        j = i
        while(j > 0 and array[j-1] > temp):
            array[j]= array[j-1]
            print(j,array)
            j -= 1
        array[j] = temp
        print(j,array,'#')
    return array
#print(insert_sort([0,1,8,5,6]))



#完全数 所有除数相加为本数6, 28, 496,8128
#28=1+2+4+7+14
#错误完全数24 = 1 + 2 + 3 + 4 + 6 + 8
#找出小于num的所有完全数
def perfect_number(number):
    start = datetime.datetime.now()
    lcount = 0
    for num in range(number+1):
        total = 1
        tstr = str(num) + ' = ' 
        div = 2
        div_high = num
        while (div < div_high):
            lcount += 1
            if (num % div == 0):
                div_high = num // div
                total += div + div_high
                tstr = tstr + " {0} + {1} ".format(div,div_high)
            div += 1
        if total == num and total>1:
             print(tstr)
    
    diff = datetime.datetime.now() - start     
    pprint(start)  
    pprint(diff)
    print("loop count: {0} cost time: {1}".format(lcount, diff.seconds))
    
    
perfect_number(10000)    

 
#sys.exit('bye!');

########################二叉树#####################################################
tree = {

'left': {'left': {'node': 'D'},
        'node': 'B',
        'right': {'node': 'E', 'left': {'node': 'H'}}},
'node': 'A',
'right':{'left': {'node': 'F', 'right': {'node': 'I'}},
        'node': 'C',
        'right': {'node': 'G'}}
}

pprint(tree)

def node_first(tree):
    temp.append(tree['node'])
    if 'left' in tree:
        node_first(tree['left'])
    if 'right' in tree:
        node_first(tree['right'])

#node_first(tree)

def node_last(tree):
    global temp
    if 'left' in tree:
        node_last(tree['left'])
    if 'right' in tree:
        node_last(tree['right'])
    temp.append(tree['node'])

#node_last(tree)

temp=[]
def node_middle(tree):
    global temp
    if 'left' in tree:
        node_middle(tree['left'])
    temp.append(tree['node'])
    if 'right' in tree:
        node_middle(tree['right'])

node_middle(tree)
print('midl:', temp)


def node_middle_loop(tree):
    visited = []
    temp = []
    while(tree or temp):
        if tree:
            temp.append(tree)

        if (tree and 'left' in tree):
            tree = tree['left']
        else:
            tree = temp.pop()
            visited.append(tree['node'])
            if 'right' in tree:
                tree = tree['right']
            else:
    #不把这个设为None,会重新把tree压进，死循环
    #已经访问到了右子树，说明这个树左中已经访问过了，不需要了
                tree = None
    #要么每次在压stack和left前检查visted
    print(visited)


node_middle_loop(tree)

pprint(tree)

#['A', 'B', 'D', 'E', 'H', 'C', 'F', 'I', 'G']
def node_first_loop(tree):
    visited = []
    temp = []
    while(tree or temp):
        if tree:
            visited.append(tree['node'])

            if ('right' in tree):
                temp.append(tree['right'])
            if ('left' in tree):
                tree = tree['left']
            elif temp:
                tree = temp.pop()
            else:
                tree = None

    print(visited)


node_first_loop(tree)

#['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I']
#非递归式读法，从上到下，从左到右，不能使用Stack而使用queque
def top_down_loop(tree):
    visited = []
    temp = [tree]
    while(temp):
        tree = temp.pop(0)
        if tree:
            visited.append(tree['node'])
            if ('left' in tree):
                temp.append(tree['left'])

            if ('right' in tree):
                temp.append(tree['right'])


    print(visited)

top_down_loop(tree);


