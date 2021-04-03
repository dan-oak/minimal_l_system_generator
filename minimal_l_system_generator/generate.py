from llist import dllist


def generate(init: str, rules: dict, n: int):
    l = dllist(init)
    for i in range(n):
        curr = l.first
        while curr is not None:
            rhs = rules[curr.value]
            for c in rhs:
                l.insert(c, curr)
            prev = curr
            curr = curr.next
            l.remove(prev)

    return ''.join(v for v in l)
