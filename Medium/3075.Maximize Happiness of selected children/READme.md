# 3075. Maximize Happiness of Selected Children

## 📝 Problem Description
You are given an array `happiness` of length `n`, and a positive integer `k`. There are `n` children standing in a queue, where the `i-th` child has happiness value `happiness[i]`. You want to select `k` children from these `n` children in `k` turns.

In each turn, when you select a child, the happiness value of all the children that have **not** been selected yet decreases by `1`. Note that the happiness value cannot become negative and is only decremented if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting `k` children.

**Link to Problem:** [Maximize Happiness of Selected Children](https://leetcode.com/problems/maximize-happiness-of-selected-children/)

---

## 🚀 Approach: Optimized Greedy
The goal is to maximize the sum, so we naturally want to pick the children with the highest initial happiness first. 

### Key Steps:
1. **Sort in Descending Order:** By sorting the array from largest to smallest, we ensure that in each turn $i$ (from $0$ to $k-1$), we are looking at the best possible candidate.
2. **Apply Decrement:** For the $i$-th child selected, their actual happiness contributed to the total is `happiness[i] - i`.
3. **Early Termination:** Since the array is sorted, if at any point `happiness[i] - i <= 0`, we can stop immediately because all subsequent children will also contribute $0$ happiness.

## 📊 Performance
- **Runtime:** 11 ms (Beats 91.67% of users)
- **Memory:** 35.58 MB

## 🛠️ Complexity Analysis
- **Time Complexity:** $O(n \log n)$ due to the initial sorting. The selection loop runs in $O(k)$.
- **Space Complexity:** $O(1)$ (ignoring the space used by the sorting algorithm).
