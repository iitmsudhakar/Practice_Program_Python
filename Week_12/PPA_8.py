def depth(exp):
    m_depth = 0
    k = 0
    for c in exp:
        if c == '(':
            k += 1
        elif c == ')':
            k -= 1
    if k > m_depth:
        m_depth = k
    return m_depth

print(depth('(()(()))()'))
