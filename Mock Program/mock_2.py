def domain_fun(domain, fun):
    keys = []
    for x in fun:
        keys.append(x)
    key_len = len(keys)
    dom_len = len(domain)
    if key_len == dom_len:
        for i in range(dom_len):
            flag = False
            if domain[i] in keys:
                flag = True
        if flag:
            return True
        else:
            return False
    else:
        return False


def codom_fun(codomain, fun):
    value = []
    for x in fun:
        val = fun[x]
        value.append(val)
    for i in range(len(value)):
        flag = False
        if value[i] in codomain:
            flag = True
    if flag:
        return True
    else:
        return False


def is_function(domain, codomain, fun):
    if domain_fun(domain, fun) and codom_fun(codomain, fun):
        return True
    else:
        return False


domain = [1, 2, 3]
codomain = [5, 6, 7]
fun = {1: 5, 2: 6, 4: 7}

print(is_function(domain, codomain, fun))
#print(domain_fun(domain, fun))
#print(codom_fun(codomain, fun))
