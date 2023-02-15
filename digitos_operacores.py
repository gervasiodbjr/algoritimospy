
def more_significative_dig(n):
    if n < 10:
        return n
    else:
        return more_significative_dig(n // 10)
    
def less_significative_dig(n):
    if n < 10:
        return n
    else:
        return less_significative_dig(n % 10)

def count_dig(n):
    if n < 10:
        return 1
    return 1 + count_dig(n // 10)

def sum_dig(n):
    if n < 10:
        return n
    return sum_dig(n // 10) + sum_dig(n % 10)

def media_digitos(n):
    return sum_dig(n) / count_dig(n)
    
# print(media_digitos(3456))      # 4.5
# print(media_digitos(34567))     # 5.0
# print(media_digitos(345678))    # 5.5

print(more_significative_dig(345678))      # 3
print(less_significative_dig(345678))     # 8
print(count_dig(345678))    # 6
print(sum_dig(345678))    # 33
print(media_digitos(345678))    # 5.5