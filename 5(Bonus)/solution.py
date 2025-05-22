import numpy as np

M,N= map(int, input().split())

weights = list(map(float, input().split()))


locations = np.array([
    list(map(int, input().split()))
    for i in range(M)
], dtype=int)

winner_idx = np.full((N, N, N), -1, dtype=int)
max_weight  = np.zeros((N, N, N), dtype=float)

for idx in range(M):
    i, j, k = locations[idx]
    if weights[idx] > max_weight[i, j, k]:
        max_weight[i, j, k] = weights[idx]
        winner_idx[i, j, k] = idx
    elif weights[idx] == max_weight[i, j, k]:
       winner_idx[i, j, k] = -2  

survivors = np.unique(winner_idx[winner_idx >= 0])

print(*survivors.tolist())
