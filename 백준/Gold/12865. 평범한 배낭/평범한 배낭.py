import sys; input = sys.stdin.readline


N, K = map(int, input().split())
K += 1

bag = {0: 0}
data = []
for _ in range(N):
    a, b = map(int, input().split())
    data.append((b, a))
# data = [tuple(map(int,input().split())) for _ in range(N)]

data.sort(reverse=True)


for v, w in data:
    tmp = {}
    for v_bag, w_bag in bag.items():
        if bag.get(nv := v + v_bag, K) > (nw := w + w_bag):
            tmp[nv]=nw
    bag.update(tmp)

print(max(bag.keys()))