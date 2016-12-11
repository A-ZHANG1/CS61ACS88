#CS61A,CS88
#Textbook from http://composingprograms.com/


#######Local state,Recursion Text book#############################
# def outer(f,x):
#     def inner():
#         return f(x)
#     return inner
# g=outer(min,[5,6])
# print(g())


# def outer(f,x):
#     return inner
# def inner():
#     return f(x)
# g=outer(min,[5,6])
# print(g())

# def letters_generator():
#     current='a'
#     while current<='d':
#         yield current
#         current=chr(ord(current)+1)
#
# letters=letters_generator()
# type(letters)
#
# caps=map(lambda x:x.upper(),b_to_k)


# def cascade(n):
#         """Print a cascade of prefixes of n."""
#         print(n)
#         if n >= 10:
#             cascade(n//10)
#             print(n)
#
# cascade(1234)

# def inverse_cascade(n):
#     grow(n)
#     print(n)
#     shrink(n)
# def f_then_g(f,g,n):
#     if n:
#         f(n)
#         g(n)
# grow=lambda n:f_then_g(grow,print,n//10)
# shrink=lambda n:f_then_g(print,shrink,n//10)

# def split(n):
#     return n//10,n%10
# def sum_digits(n):
#     if n<10:
#         return n
#     else:
#         all_but_last,last=split(n)
#         return sum_digits(all_but_last)+last
# def luhm_sum(n):
#     if n<10:
#         return n
#     else:
#         all_but_last,last=split(n)
#         return luhm_sum_double(all_but_last)+last
# def luhm_sum_double(n):
#     all_but_last,last=split(n)
#     luhm_digit=luhm_sum(2*last)
#     if n<10:
#         return luhm_digit
#     else:
#         return luhm_sum(all_but_last)+luhm_digit
# print(luhm_sum(32))

# def partitions(n,m):
#     if n==0:
#         return Link(Link.empty)
#     elif n<0 or m==0:
#         return Link.empty
#     else:
#         using_m=partitions(n-m,m)
#         with_m=map_link(lambda s:Link(s,m),using_m)
#         without_m=partitions(n,m-1)
#         return with_m+without_m


# def reduce(reduce_fn,s,initial):#!!
#     reduced=initial
#     for x in s:
#         redudced=reduce_fn(redudced,x)
#     return reduced
# reduce(mul,[2,4,8],1)

####2.3 tree from textbook#################################
# def tree(root,branches=[]):#!!
#     for branch in branches:
#         assert is_tree(branch),'Branch must be a tree.'
#     return [root]+list(branches)
# def root(tree):
#     return tree[0]
# def branches(tree):
#     return tree[1:]
# def is_tree(t):#!!
#     if type(t) is not list or len(t)<0:
#         return False
#     for branch in branches(t):
#         if not is_tree(branch):
#             return False
#     return True
# def is_leaf(tree):
#     return not branches(tree)
# ####general parts for tree implementation ends#
# ####specific functioning functions begins######
# # def fib_tree(n):#!!
# #     if n==0 or n==1:
# #         return tree(n)
# #     else:
# #         left,right=fib_tree(n-1),fib_tree(n-2)
# #         fib_n= root(left)+root(right)
# #         return tree(fib_n,[left,right])
# # print(fib_tree(5))#!!
# #
# # def partition_tree(n,m):
# #     if n==0:
# #         return tree(True)#!!
# #     if n<0 or m==0:
# #         return tree(False)#!!
# #     left=partition_tree(n-m,m)
# #     right=partition_tree(n,m-1)
# #     return tree(m,[left,right])#!!
# # def print_parts(tree,partition=[]):
# #     if is_leaf(tree):#
# #         #if root(tree):#??
# #             print('+'.join(partition))#a string
# #         #method takes a list of things to join with the string.
# #     else:
# #         left,right=branches(tree)
# #         m=str(root(tree))
# #         print_parts(left,partition+[m])
# #         print_parts(right,partition)
# # print_parts(partition_tree(6,4))
# #
# # def right_binarize(tree):
# #     if is_leaf(tree):
# #         return tree
# #     if len(tree)>2:
# #         tree=[tree[0],tree[1:]]
# #     return [right_binarize(b) for b in tree]
# # print(right_binarize([1,2,3,4,5,6,7]))
# ###2.3 tree####################################
#
# ##hw5 tree#####################################
# def print_tree(t,indent=0):
#     print(' '*indent+str(root(t)))
#     for branch in branches(t):
#         print_tree(branch,indent+1)
# print_tree(tree(1,[tree(2)]))
#
# def make_pytunes(username):
#     return tree(username,[tree('pop',[tree('justinbieber',[tree('single',[tree('what do you mean?')])]),tree('105 pop mashup')]),
#                             tree('trace',[tree('darude',[tree('sandstorm')])])])
# print_tree(make_pytunes('I love music'))
#
# def num_leaves(t):
#     if is_leaf(t):
#         return 1
#     else:
#         #return 1+num_leaves(branches(t))??
#         return sum([num_leaves(branch) for branch in branches(t)])
# print(num_leaves(make_pytunes('music')))
#
# def num_leaves_2(t):
#     if is_leaf(t):
#         return 1
#     else:
#         leaves=0
#         for b in branches(t):
#             leaves+=num_leaves_2(b)
#         return leaves
# print(num_leaves_2(make_pytunes('music')))
#
# ###crtl+F#######################
# def find(t,target):
#     if root(t)==target:
#         return True
#     else:
#         return any([find(branch,target) for branch in branches(t)])#
# def find_2(t,target):
#     if root(t)==target:
#         return True
#     else:
#         for branch in branches(t):
#             if find(branch,target):
#                 return True
#         return False
# my_account = tree('kpop_king',
#                         [tree('korean',
#                              [tree('gangnam style'),
#                                tree('wedding dress')]),
#                          tree('pop',
#                                [tree('t-swift',
#                                     [tree('blank space')]),
#                                 tree('uptown funk'),
#                                 tree('see you again')])])
# print(find(my_account, 'bad blood'))
#
# ###add to tree#################
# def add_song(t,song,category):
#     if root(t)==category:
#         return tree(category,branches(t)+[tree(song)])
#     else:
#         #for b in branches(t):
#             #all_branches=add_song(b,song,category)
#         #link! jianya!
#         return tree(root(t),[add_song(b,song,category) for b in branches(t)])
# ##test#######################
# indie_tunes = tree('indie_tunes',
#                       [tree('indie',
#                         [tree('vance joy',
#                            [tree('riptide')])])])
# new_indie = add_song(indie_tunes, 'georgia', 'vance joy')
# print_tree(new_indie)
#
# ####delete###################
# def delete(t, target):
#     kept_branches=[b for b in branches(t) if root(b)!=target]
#     return tree(root(t),kept_branches)
# ######test##################
# my_account = tree('kpop_king',[tree('korean',[tree('gangnam style'),tree('wedding dress')]),tree('pop',[tree('t-swift',[tree('blank space')]),tree('uptown funk'),tree('see you again')])])
# new = delete(my_account, 'pop')
# print_tree(new)
#
# ###mutable#################
# #not passing test because nonloca not available in python 2.x#
# def make_withdraw(balance, password):
#     attempt=[]#!!
#     def withdraw(amount,p):
#         nonlocal balance#!!
#         for i in range(3):
#             if p!=password:
#                 attempt+=[p]
#             else:
#                 break;
#             if i==3:
#                 return "Your account is locked. Attempts: "+str(attempt)
#             if amount > d['y']:
#                 return 'Insufficient funds'
#                 d['y'] = d['y'] - amount
#                 print(d['y'])
#     return withdraw
# ##
#
# def make_joint(withdraw, old_password, new_password):
#     error = withdraw(0,old_passord)
#     if type(error)==str:#nice way to decide whether return value is a 'insufficient funds'or valid amount
#         return error
#     def joint(amount,password_attempt):#READ the question
#         if password_attempt==new_password:
#             return withdraw(amount,old_passord)
#         return withdraw(amount,password_attempt)
#     return joint

##dispatch dictionary################################
 #abstract data type : account
# def account(initial_balance):#constructor
#     def deposit(amount):
#         dispatch['balance'] += amount
#         return dispatch['balance']
#     def withdraw(amount):
#         if amount > dispatch['balance']:
#             return 'Insufficient funds'
#         dispatch['balance'] -= amount
#         return dispatch['balance']
#     dispatch = {'deposit':   deposit, #store the local state of account
#                 'withdraw':  withdraw,
#                 'balance':   initial_balance}
#             #  message   :   number or functions
#             #functions here have access to the dispatch library
#             #thus can read or write balance
#     return dispatch
#
# def withdraw(account, amount):#function to withdraw
#     return account['withdraw'](amount)
# def deposit(account, amount):#function to withdraw
#     return account['deposit'](amount)
# def check_balance(account):#selector
#     return account['balance']
#####test##########################
# a = account(20)
# deposit(a, 5)
# withdraw(a, 17)
# print(check_balance(a))

##########text book 2.3.7 linked list########################
empty='empty'
def is_link(s):
    return s is empty or len(s)==2 and is_link(s[1])
def link(first,rest):
    assert is_link(rest)
    return [first,rest]
def first(s):
    assert is_link(s)
    assert s!=empty
    return s[0]
def rest(s):
    assert is_link(s)
    assert s!=empty
    return s[1]
four=link(1,link(2,link(3,link(4,empty))))
print(is_link(four))
print(rest(four))
print(first(four))

def len_link(s):#don't use the name 'len' for it's internally defined
    if s is empty:
        return 0
    return len_link(rest(s))+1

# def len_link(s):
#     length=0
#     while s is not empty:
#         s=rest(s)
#         length+=1
#     return length
print(len_link(four))

def getitem_link(s,i):
    while i !=1:
        s,i=rest(s),i-1
    return first#not s[0] (abstraction barrier)
print(getitem_link(four,2))

def extend_link(s,t):
    head=s
    while rest(s) != empty:
        s=rest(s)
    link(first(s),t)

###OOP Textbook 2.5 2.6 2.9###########################################
# def make_instance(cls):
#     def get_value(name):
#         if name i attributes:
#             return attributes[name]
#         else:
#             value = cls['get'](name)#??
#             return bind_method(value,instance)
#     def set_value(name,value):
#         attributes[name]=value
#         attributes={}
#         instance={'get':get_}
