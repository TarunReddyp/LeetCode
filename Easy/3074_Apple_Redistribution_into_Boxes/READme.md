# 3074. Apple Redistribution into Boxes 🍎📦

## 🚀 Performance
- **Runtime:** 0 ms (Beats 100.00% of Python submissions)
- **Memory:** 12.30 MB (Beats 100.00% of Python submissions)

## 📝 Problem Description
You are given an array `apple` of size `n` and an array `capacity` of size `m`. There are `n` packs of apples, where the `i-th` pack contains `apple[i]` apples. There are `m` empty boxes as well, where the `i-th` box has a capacity of `capacity[i]` apples.

The goal is to find the **minimum number of boxes** you need to select to redistribute all the apples from the packs into these boxes.

## 💡 Logic & Approach
This is a **Greedy Algorithm** problem. Since we can split apples from a single pack into multiple boxes, the size of individual apple packs is irrelevant—only the **total sum** of apples matters.

1. **Calculate Total Apples:** Sum all values in the `apple` array.
2. **Sort Capacities:** Sort the `capacity` array in descending order (largest to smallest).
3. **Greedy Selection:** Iterate through the sorted capacities and subtract each box's capacity from the total apple count.
4. **Efficiency:** By using the largest boxes first, we mathematically guarantee the minimum number of boxes used.

## 📊 Complexity Analysis
- **Time Complexity:** $O(n + m \log m)$ where $n$ is the number of apple packs and $m$ is the number of boxes.
- **Space Complexity:** $O(1)$ (excluding sorting overhead).
