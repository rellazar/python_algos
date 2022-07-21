#recursive sigma

def re_sig (num):
    if num > 0:
        return re_sig(num-1) + num
    return(0)
print(re_sig(5))

#recursive factorial

def re_fac(num:int)->int:
    num = int(num)
    if num == 0:
        return 1
    return factorial(num - 1) * num

print(re_fac(3))
print(re_fac(6.5))