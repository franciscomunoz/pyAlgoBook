"""Describe and alalyze a natural join of a list A of n pairs and a list B of m
pairs."""

def natural_join(table1,table2):
    """Merged tables will be placed in a list of lists""" 
    join = []
    if len(table1) != len(table2):
        return
    else:
        for i in range(len(table1)):
            if table1[i][1] == table2[i][0]:
                join.append([table1[i][0],table1[i][1],table2[i][1]])
            else:
                return
    return join
    
if __name__ == '__main__':

    tests = []
    table1 = [
                ('brand1','loan1'),
                ('brand2','loan2'),
                ('brand3','loan3'),
                ('brand4','loan4'),
                ('brand5','loan5')
             ]
    table2 = [
                ('loan1','cost1'),
                ('loan2','cost2'),
                ('loan3','cost3'),
                ('loan4','cost4'),
                ('loan5','cost5')
             ]

    tables = [table1, table2]

    tests.append(tables)
    """Error scenario""" 
    table1 = [
                ('brand1','loan1'),
                ('brand2','loan2'),
                ('brand3','savins3'),
                ('brand4','loan4'),
                ('brand5','loan5')
             ]
    table2 = [
                ('loan1','cost1'),
                ('loan2','cost2'),
                ('loan3','cost3'),
                ('loan4','cost4'),
                ('loan5','cost5')
             ]

    tables = [table1, table2]

    tests.append(tables)

    for i in range(len(tests)):
        result = natural_join(tests[i][0],tests[i][1])
        print("Test {0} was ".format(i),end="")
        print("NOT able to join the table due to element mismatch")\
                if not result  else\
        print("able to join the tables : {0}".format(result))
    
