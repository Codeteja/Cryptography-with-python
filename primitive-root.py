# python programme to find primitive roots modulo n

def is_primitive_root(a, n):
    for i in range(1, n):
        if pow(a, i, n) == 1:
            return False
    return True

def find_primitive_roots(n):
    prim_roots = []
    for a in range(2, n):
        if is_primitive_root(a, n):
            prim_roots.append(a)
    return prim_roots

# Example usage
result = find_primitive_roots(15)
print(result)
