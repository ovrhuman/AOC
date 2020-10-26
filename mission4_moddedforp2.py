# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 09:28:40 2020

@author: bobby
"""

#password range
min_pw = 284639
max_pw = 748759


def list_to_num(x):
    stringy = ''
    for n in x:
        stringy += str(n)
    return int(stringy)


password = [0,0,0,0,0,0]
pwlist = []
pw_counter = 0

for p in range(0,len(password)-1):
    password = [0,0,0,0,0,0]
    if p == 0:
        for i in range(10):
            password=[0,0,0,0,0,0]
            password[p] = i
            password[p+1] = i 
            for j in range(password[p+1],10):
                password[2] = j
                for k in range(j,10):
                    password[3] = k
                    for l in range(k,10):
                        password[4] = l
                        for m in range(l,10):
                            password[5] = m
                            if list_to_num(password) > max_pw:
                                break
                            elif list_to_num(password) >= min_pw:
                                if not password[p+2] == password[p+1]:   #remove these if statements to revert to part 1 
                                    pw_counter += 1
                                    pwlist.append(password.copy())
                            

    if p == 1:
          for i in range(10):
            password=[0,0,0,0,0,0]
            password[p] = i
            password[p+1] = i 
            for j in range(0,password[p]):
                password[0] = j
                for k in range(password[p+1],10):
                        password[3] = k
                        for l in range(k,10):
                            password[4] = l
                            for m in range(l,10):
                                password[5] = m
                                if list_to_num(password) > max_pw:
                                    break  
                                elif list_to_num(password) >= min_pw:
                                    if not password[p+2] == password[p+1] and not password[p-1] == password[p]:
                                        pw_counter += 1
                                        pwlist.append(password.copy())
    
    if p == 2:
         for i in range(10):
            password=[0,0,0,0,0,0]
            password[p] = i
            password[p+1] = i 
            for j in range(0, password[p]+1):
                password[0] = j
                for k in range(j,password[p]+1):
                    password[1] = k
                    for l in range(password[p+1],10):
                        password[4] = l
                        for m in range(l,10):
                            password[5] = m
                            if list_to_num(password) > max_pw:
                                break    
                            elif list_to_num(password) >= min_pw:
                                if not password[p+2] == password[p+1] and not password[p-1] == password[p]:
                                        pw_counter += 1
                                        pwlist.append(password.copy())
                            
    if p == 3:
        for i in range(10):
            password=[0,0,0,0,0,0]
            password[p] = i
            password[p+1] = i 
            for j in range(0,password[p]+1):
                password[0] = j
                for k in range(j,password[p]+1):
                    password[1] = k
                    for l in range(k,password[p]+1):
                        password[2] = l
                        for m in range(password[p+1],10):
                            password[5] = m
                            if list_to_num(password) > max_pw:
                                break  
                            elif list_to_num(password) >= min_pw:
                                if not password[p+2] == password[p+1] and not password[p-1] == password[p]:
                                        pw_counter += 1
                                        pwlist.append(password.copy())
                            
    if p == 4:
        for i in range(10):
            password=[0,0,0,0,0,0]
            password[p] = i
            password[p+1] = i 
            for j in range(0, password[p]+1):
                password[0] = j
                for k in range(j,password[p]+1):
                    password[1] = k
                    for l in range(k,password[p]+1):
                        password[2] = l
                        for m in range(k,password[p]+1):
                            password[3] = m
                            if list_to_num(password) > max_pw:
                                break  
                            if list_to_num(password) >= min_pw:
                                if not password[p-1] == password[p]:
                                        pw_counter += 1
                                        pwlist.append(password.copy())
                                
pwtuple = [tuple(x) for x in pwlist] 
pwset = set(pwtuple)
cleanpw = [x for x in pwset if x[0] <= x[1] and x[1] <= x[2] and x[2] <= x[3] and x[3] <= x[4] and x[4] <= x[5]]
      