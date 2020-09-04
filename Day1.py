# LIST AND ITS FUNCTIONS
lst = [1, 2, 3, 4, 5]
print(lst)
lst.sort()
print(lst)
lst.append(100)
print(lst)
print(lst.count(100))
lst.reverse()
print(lst)
lst.pop()
print(lst)

# DICTIONARY AND ITS FUNCTIONS
dt = {"name": "Deepansh", "l_name": "agrawal", "age": 20}
print(dt)
print(dt.keys())
print(dt.items())
print(dt.__len__())
dt.pop("age")
print(dt)
dt2 = dt.copy()
print(dt2)

# SETS ANS ITS DEFAULT FUNCTIONS
st = {12, 43, 100, 45, 123, 65, 34688}
print(st)
st.pop()
print(st)
st2 = {345, 67, 789}
st3 = st.union(st2)
print(st3)
st2.update(st)
print(st2)
st2.discard(345)
print(st2)
print(st.isdisjoint(st2))

# Tuple and its Functions
tp = (1, 2, 5, 100, 54, 678)
print(tp)
print(tp.count(100))
print(tp.index(5))
print(tp.__getitem__(4))

# String and its Functions
st = "dEEPANSH"
print(st.strip())
print(st.lower())
print(st.upper())
print(st.count("A"))
print(st.isdigit())