# =============================================================================
# #1
# A=['python', 'php', 'java']
# for i in range(0, len(A)):
#     print(A[i])
# =============================================================================
# =============================================================================
# # 2
# A=[1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in range(0, len(A)):
#     sum += A[i]
# print(sum)
# =============================================================================
# =============================================================================
# #3
# A=[1,2,3,4,5]
# x=1
# k=0
# while len(A)>k:
#     x=x*A[k]
#     k+=1
# print(x)
# =============================================================================
# =============================================================================
# # 4
# B=[2,4,6,8,10]
# print(B[2]*B[-1])
# =============================================================================
# =============================================================================
# #5
# B=(1,2,3,4,5)
# print(max(B))
# print(min(B))
# =============================================================================
# =============================================================================
# # 6
# C= ['abdba', 'abcd', '121']
# a= 0
# for i in C:
#     if len(i)>2 and i[0] == i[-1]:
#         a+=1
# print(a)
# =============================================================================
# =============================================================================
# =============================================================================
# # #7
# # C = ['abdba', 'abcd', '121', '121', 'abcd' ]
# # D=list(set(C))
# # print(D)
# =============================================================================
# =============================================================================
# =============================================================================
# # 8
# D = []
# if len(D) == 0:
#     print("Hooson")
# else:
#     print("Hooson bish")
# =============================================================================
# =============================================================================
# #9
# E=[1,2,3,4,5,6,7,8,9,10]
# print(len(E))
# E.pop(3)
# E.pop(5)
# E.pop(-3)
# print(E)
# =============================================================================
# =============================================================================
# # 10
# E=(1,3,6,9)
# =============================================================================
# =============================================================================
# #11
# F=()
# G=list(F)
# G.append(input())
# F=tuple(G)
# print(F)
# =============================================================================
# =============================================================================
# # 12
# F=('a','b','c','d','e')
# print(F[1],F[-2])
# =============================================================================
# =============================================================================
# #13
# F=(1,2,3,4)
# a=int(input())
# if a in F:
# 	print('yes')
# else:
#     print('no')
# =============================================================================
# =============================================================================
# # 14
# G=('a','b','c','d','e')
# k = 0
# while len(G)>k:
#     print(G[k])
#     k += 1
# =============================================================================
# =============================================================================
# #15
# I={1,2,3}
# J={2,3,4,5}
# Merge=I.union(J)
# print(Merge)
# print(I)
# =============================================================================
# =============================================================================
# # 16
# Num= {'1', '2', '3', '4', 'y'} 
# Let= {'2', 'x', 'y'} 
# Newset = Num.intersection(Let)
# print(Newset)
# =============================================================================
# =============================================================================
# #17
# L={1,2,3,4,5}
# print(len(L))
# =============================================================================
# =============================================================================
# =============================================================================
# # 18
# L= {'a', 'b', 'c', 'd','e'}
# L.remove(input())
# print(L)
# =============================================================================
# #19
# M={1,2,3,4,5}
# M.clear()
# print(M)
# =============================================================================
# =============================================================================
# # 20
# fruits= {'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'}
# del fruits
# =============================================================================
# =============================================================================
# #21
# P = { 
# 	'1': 80, 
# 	'2': 99} 
# if P['1']>P['2']:
#     print('Буурах:',P['1'],P['2'])
#     print('Өсөх:',P['2'],P['1'])
# else:
#     print('Буурах:',P['2'],P['1'])
#     print('Өсөх:',P['1'],P['2'])
# =============================================================================
# =============================================================================
# #21 Боломж 2
# P={
#    1:80, 
#    2:99, 
#    3:77 } 
# A= list(P.keys())
# B= list(P.values())
# C=A+B
# C.sort()
# print('Өсөх:',C)
# C.sort(reverse=True)
# print('Буурах:',C)    
# =============================================================================
# =============================================================================
# # 22
# Q= { 
#     'Нэр': 'Нинжин', 
#     'Оюутны код': 'b20fa1202', 
#     'Нас': 20 } 
# if 'Нэр' in Q:
#     print('Нэр жагсаалтад байна' )
# =============================================================================

# =============================================================================
# #23
# Q={ 
#    'Нэр': 'Нинжин' 
#    'Оюутны код': 'b20fa1202', 
#    'Нас': 20}  
# if b20fa1202 in Q.values():
#     print('Байна' )
# else:
#     print('Байхгүй')
# =============================================================================
# =============================================================================
# # 24
# Q = { 
#     'Нэр': 'Нинжин', 
#     'Оюутны код': 'b20fa1202', 
#     'Нас': 20 } 
# for x,y in Q.items():
#     print(x,y)
# =============================================================================
# =============================================================================
# #25
# Q={ 
#    'Нэр': 'Нинжин', 
#    'Оюутны код': 'b20fa1202', 
#    'Нас': 20} 
# R={ 
#    'Он': 2022, 
#    'Сар': 'Feb', 
#    'Өдөр': 'Sunday'} 
# Q.update(R)
# print(Q)
# =============================================================================
# =============================================================================
# # 26
# Q= {
#     'Он': 2022, 
#     'Сар':2, 
#     'Өдөр': 20 } 
# sum=0
# for i in Q:
#     sum += Q[i]
# print(sum)
# =============================================================================





















