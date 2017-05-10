"""Modify Code Fragment 6.5 so that it can properly match tags, even when an 
opening tag may include one or more such attributes."""


from exceptions import Empty
from exceptions import Full

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self, maxlen = None):
        """Create an empty stack."""
        self._data = []                       # nonpublic list instance
        self._maxlen = maxlen

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        if self._maxlen != None and len(self._data) >= self._maxlen:
            raise Full('Stack is full')
        self._data.append(e)                  # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()               # remove last item from list


def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find('<')               # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j+1)        # find next '>' character
        if k == -1:
            return False                # invalid tag
        tag = raw[j+1:k]              # strip away < >
        if not tag.startswith('/'):   # this is opening tag
            s = tag.find(' ')         #we find space in case of tag properties	
            if s == -1:
                S.push(tag)                 
            else:
                S.push(tag[:s])       #ignore tag properties and push it
        else:                         # this is closing tag
            if S.is_empty():
                return False              # nothing to match with
            if tag[1:] != S.pop():   
                return False              # mismatched delimiter
        j = raw.find('<', k+1)        # find next '<' character (if any)
    return S.is_empty()             # were all opening tags matched?



if __name__ == '__main__':
	raw = """<html>
	    <head>
	    <title>HTML table Tag</title>
	    </head>
	    <body>
	    <table border="1">
	      <tr>
		<th>Team</th>
		<th>Ranking</th>
	      </tr>
	      <tr>
		<td>India</td>
		<td>1</td>
	      </tr>
	      <tr>
		<td>South Africa</td>
		<td>2</td>
	      </tr>
	      <tr>
		<td>Australia</td>
		<td>3</td>
	      </tr>
	    </table>
	    </body>
	    </html>"""

	import pdb;pdb.set_trace()
	print("Are the html tags matching : {0}".format(is_matched_html(raw))) 
