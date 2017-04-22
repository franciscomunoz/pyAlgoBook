"""Write a Python function that takes two three-dimensional numeric data sets
and adds them componentwise"""
import pprint

def add_component_wise(ds1, ds2, n):
    """This implementation assumes dimensions match"""
    result  = [ [ [0 for k  in range(n)] for j in range(n) ] for i in range(n) ] 
    
    result = [ [ [ds1[i][j][k] + ds2[i][j][k] for k in range(n)] \
            for j in range(n) ] for i in range(n) ] 
    return result


if __name__ == '__main__':

    n = 3

    data1 = [ [ [k for k in range(n)] for j in range(n) ] for i in range(n) ] 

    data2 = [ [ [2 * k for k in range(n)] for j in range(n) ] for i in range(n) ] 

    result = add_component_wise(data1, data2, n)

    pprint.pprint("The result of adding two 3d arrays is : {0}".format(result))
