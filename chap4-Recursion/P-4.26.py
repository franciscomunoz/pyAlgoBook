"""Simple recursive function for the towers of hannoi puzzle"""


def movedisk(source,destiny,k):
    if k == 0:
        return
    else:
        destiny.append(source[-1])
        del source[-1]
        movedisk(source,destiny,k-1)

if __name__ == '__main__':
    peg_a = ['*','**','***','****']
    peg_b = []
    peg_c = []

    """Move k - 1 disk to peg b"""
    movedisk(peg_a,peg_b,len(peg_a)-1)
    """Move remaining disk to peg c"""
    movedisk(peg_a,peg_c,len(peg_a))
    """Move k - 1 disk from peg b to c"""
    movedisk(peg_b,peg_c,len(peg_b))
    for i in peg_c:
        print(i)
