# 移出重复项且元素间顺序不变
# 用set解决


def deldup(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 2, 3, 4, 5, 7, 4, 21, 1, 2, 4, 5, 7]
b = list(deldup(a))
print(b)
