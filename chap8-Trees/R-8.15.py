"""The  LinkedBinary Tree class provides only nonpublic versions of the update 
methods discussed on page 319. Implement a simple subclass named MutableLinkedTree
that provides public wrapper functions for each of the inherited nonpublic update
methods."""

class MutableLinkedBinaryTree(LinkedBinaryTree):

    def __init(self, parent=None, left=None, right=None):
        """Forward params to parent class"""
        super().__init__(parent, left, right)

    def add_root(self, e):
        """Public method for _add_root"""
        return self.add_root(e)

    def add_left(self, p, e):
        """Public method for _add_left"""
        return self._add_left(p,e) 

    def add_right(self, p, e):
        """Public method for _add_right"""
        return self._add_right(p, e) 

    def replace(self,p e):
        """Replace element stored in position p by element e"""
        return self._replace(p, e)

    def delete(self, p):
        """Removes the node at position p (see private implementation)"""
        return self._delete(p)

    def attach(self, p, T1, T2):
        """Attach the internal structure of trees T1 and T2, respectively
        (see private implementation)"""
        return self._attach(p, T1, T2)



       


    
