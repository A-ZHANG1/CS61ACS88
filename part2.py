"""
####Recursive object(Text 2.9.1)--Linked list+lab7#################
"""
class Link:
    empty=()#tuple
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)#Link.empty!
        self.first=first
        self.rest=rest
    def __len__(self):
        return 1+len(self.rest)
    def __getitem__(self,i):
        if i==1:
            return self.first
        else:
            return self.rest[i-1]
    def link_expression(self):
        return

s=Link(3,Link(4,Link(5)))
print(len(s))
