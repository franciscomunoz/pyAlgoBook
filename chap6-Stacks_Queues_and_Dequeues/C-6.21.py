"""Show how to use a Stack S and a queue Q to generate all posible subsets of 
an n-element set T nonrecursively """

from array_stack import ArrayStack
from array_queue import ArrayQueue
import copy

def generate_subsets(data):

    S = ArrayStack()
    Q = ArrayQueue()

    subsets = []
    #Remember ArrayQueue has default capacity of 10 
    for i in range(len(data)):
        Q.enqueue(data[i])
        S.push(data[i]) 
    #Backup queue for future rotations
    backup_queue = copy.deepcopy(Q)
    #Amount of queue rotations
    for i in range(len(data)):
        #Assemble queue once the queue has rotated for the first time
        if i != 0:
            for i in range(len(data)):
                S.push(Q.dequeue())
        count_i = 0
        count_j = 0
        #Gerate subsets 
        while (count_i < len(data) - 1):
            S2 = ArrayStack()
            subset = []
            while (count_j <= count_i):
                val = S.pop()
                subset.append(val)      
                S2.push(val)
                count_j += 1
            #Put back to stack for next subset
            while not S2.is_empty():
                S.push(S2.pop())
            
            subsets.append(subset)
            count_i += 1
            #reset count j for future subset
            count_j = 0

        #Rotate queue
        val = backup_queue.dequeue()
        backup_queue.enqueue(val)
        #Refresh queue with rotated version
        Q = copy.deepcopy(backup_queue)
    #Return a list of subsets 
    return subsets

if __name__ == '__main__':

    tests = []

    tests.append([1,2,3,4])

    for i in range(len(tests)):
        subsets = generate_subsets(tests[i])
        print("The subsets are : {0}".format(subsets))


