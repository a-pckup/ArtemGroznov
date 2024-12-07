a = [14254, 12423, 12165, 1223, 62255, 87155]

a_tr = [True if len(str(x)) == 3 else False for x in a]

print(any(a_tr))

# all() any()