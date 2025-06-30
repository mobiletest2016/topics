# Daily problems


### [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        LinkedList<Integer> stack = new LinkedList<>();
        int res = 0;
        for(int i = 0; i <= heights.length; i++) {
            int height = i == heights.length ? 0 : heights[i];
            while (!stack.isEmpty() && height <= heights[stack.peek()]) {
                int h = heights[stack.pop()];
                int w = stack.isEmpty() ? i : i - 1 - stack.peek();
                res = Math.max(res, h * w);
            }
            stack.push(i);
        }
        return res;
    }
}
```

### [283. Move Zeroes](https://leetcode.com/problems/move-zeroes)

```java
class Solution {
    public void moveZeroes(int[] nums) {
        int cnt = 0;
        for(int i = 0; i < nums.length; i++) {
            if (nums[i] == 0)
                cnt++;
            else
                nums[i - cnt] = nums[i];
        }

        for(int i = 0; i < cnt; i++)
            nums[nums.length - 1 - i] = 0;
    }
}
```


### [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)

```java
class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        Arrays.setAll(dp, t -> t);
        return numSquares(n, dp);
    }

    private int numSquares(int n, int[] dp) {
        if (n == 1)
            return 1;

        if (dp[n] < n)
            return dp[n];

        for(int i = n / 2; i > 0; i--) {
            if (i * i <= n)
                dp[n] = Math.min(dp[n], numSquares(n - i * i, dp) + 1);
        }
        return dp[n];
    }
}
```

```java
class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        Arrays.setAll(dp, t -> t);
        for(int i = 0; i <= n; i++) {
            for(int j = 0; j * j <= i; j++)
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
        }
        return dp[n];
    }
}
```

### [968. Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras)

```java
class Solution {
    final int COVERED = 1;
    final int NEED_COVER = 2;
    final int HAS_CAMERA = 0;
    int res = 0;
    public int minCameraCover(TreeNode root) {
        int ret = minCamera(root);
        if (ret == NEED_COVER)
            res++;
        return res;
    }

    private int minCamera(TreeNode root) {
        if (root == null)
            return COVERED;
        int left = minCamera(root.left);
        int right =  minCamera(root.right);
        if (left == HAS_CAMERA || right == HAS_CAMERA)
            return COVERED;
        if (left == NEED_COVER || right == NEED_COVER) {
            res++;
            return HAS_CAMERA;
        }
        return NEED_COVER;
    }
}
```

https://leetcode.com/problems/132-pattern

https://leetcode.com/problems/best-time-to-buy-and-sell-stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

https://leetcode.com/problems/candy

https://leetcode.com/problems/cheapest-flights-within-k-stops

https://leetcode.com/problems/combination-sum

https://leetcode.com/problems/combination-sum-ii

https://leetcode.com/problems/combination-sum-iii

https://leetcode.com/problems/contains-duplicate-ii

https://leetcode.com/problems/continuous-subarray-sum

https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times

https://leetcode.com/problems/diameter-of-binary-tree

https://leetcode.com/problems/distribute-candies-among-children-i

https://leetcode.com/problems/distribute-candies-among-children-ii

https://leetcode.com/problems/distribute-coins-in-binary-tree

https://leetcode.com/problems/domino-and-tromino-tiling

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

https://leetcode.com/problems/finding-3-digit-even-numbers

https://leetcode.com/problems/gas-station

https://leetcode.com/problems/implement-trie-prefix-tree

https://leetcode.com/problems/lexicographical-numbers

https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit

https://leetcode.com/problems/longest-nice-subarray

https://leetcode.com/problems/longest-repeating-character-replacement

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

https://leetcode.com/problems/lru-cache

https://leetcode.com/problems/majority-element

https://leetcode.com/problems/majority-element-ii

https://leetcode.com/problems/maximum-candies-allocated-to-k-children

https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes

https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended

https://leetcode.com/problems/maximum-subarray

https://leetcode.com/problems/maximum-width-of-binary-tree

https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful

https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

https://leetcode.com/problems/minimum-deletions-to-make-string-k-special

https://leetcode.com/problems/number-of-wonderful-substrings

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing

https://leetcode.com/problems/removing-minimum-and-maximum-from-array

https://leetcode.com/problems/repeated-substring-pattern

https://leetcode.com/problems/reveal-cards-in-increasing-order

https://leetcode.com/problems/reverse-nodes-in-k-group

https://leetcode.com/problems/rotate-array

https://leetcode.com/problems/split-array-into-consecutive-subsequences

https://leetcode.com/problems/subarray-sum-equals-k

https://leetcode.com/problems/subarray-sums-divisible-by-k
