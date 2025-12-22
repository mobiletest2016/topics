# Daily problems

### [960. Delete Columns to Make Sorted III](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/)

### [955. Delete Columns to Make Sorted II](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/)

### [2092. Find All People With Secret](https://leetcode.com/problems/find-all-people-with-secret/description/)

### [133. Clone Graph](https://leetcode.com/problems/clone-graph/)

### [189. Rotate Array](https://leetcode.com/problems/rotate-array/)

### [3583. Count Special Triplets](https://leetcode.com/problems/count-special-triplets/)

### [149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/)

### [2141. Maximum Running Time of N Computers](https://leetcode.com/problems/maximum-running-time-of-n-computers/)

### [3623. Count Number of Trapezoids I](https://leetcode.com/problems/count-number-of-trapezoids-i/)

### [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

### [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

### [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

### [3542. Minimum Operations to Convert All Elements to Zero](https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/)

### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

### [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

### [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

### [2169. Count Operations to Obtain Zero](https://leetcode.com/problems/count-operations-to-obtain-zero)

### [3607. Power Grid Maintenance](https://leetcode.com/problems/power-grid-maintenance)

### [2528. Maximize the Minimum Powered City](https://leetcode.com/problems/maximize-the-minimum-powered-city/)

### [3354. Make Array Elements Equal to Zero](https://leetcode.com/problems/make-array-elements-equal-to-zero/)

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

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights) + 1):
            height = heights[i] if i < len(heights) else 0
            while len(stack) > 0 and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if len(stack) == 0 else i - 1 - stack[-1]
                res = max(res, w * h)
            stack.append(i)
        return res
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

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                nums[i - cnt] = nums[i]
        for i in range(cnt):
            nums[len(nums) - 1 - i] = 0
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

### [3330. Find the Original Typed String I](https://leetcode.com/problems/find-the-original-typed-string-i/)

```java
class Solution {
    public int possibleStringCount(String word) {
        int res = 1;
        for(int i = 0; i < word.length(); i++) {
            if (i < word.length() - 1 && word.charAt(i) == word.charAt(i + 1))
                res++;
        }
        return res;
    }
}
```

```python
class Solution(object):
    def possibleStringCount(self, word):
        res = 1
        for i in range(len(word)):
            if i < len(word) - 1 and word[i] == word[i + 1]:
                res += 1
        return res
```

### [456. 132 Pattern](https://leetcode.com/problems/132-pattern)

```java
class Solution {
    public boolean find132pattern(int[] nums) {
        Stack<Integer> stack = new Stack<>();
        int max = Integer.MIN_VALUE;
        for(int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] < max)
                return true;

            while(!stack.isEmpty() && stack.peek() < nums[i])
                max = stack.pop();

            stack.push(nums[i]);
        }

        return false;
    }
}
```

```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mmax = float('-inf')
        for n in nums[::-1]:
            if n < mmax:
                return True
            while len(stack) > 0 and n > stack[-1]:
                mmax = max(stack.pop(), mmax)
            stack.append(n)
        return False
```

### [997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

```java
class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] cnt = new int[n + 1];

        for(int[] t : trust) {
            cnt[t[1]]++;
            cnt[t[0]]--;
        }

        for(int i = 1; i <= n; i++) {
            if (cnt[i] == n - 1)
                return i;
        }
        return -1;
    }
}
```

### [1353. Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended)

```java
class Solution {
    public int maxEvents(int[][] events) {
        Arrays.sort(events, (a, b) -> Integer.compare(a[0], b[0]));
        int lastday = 0;
        int firstday = Integer.MAX_VALUE;
        for(int[] event : events) {
            lastday = Math.max(lastday, event[1]);
            firstday = Math.min(firstday, event[0]);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int idx = 0;
        int res = 0;
        for(int day = firstday; day <= lastday; day++) {
            while(!pq.isEmpty() && pq.peek() < day)
                pq.poll();
            while(idx < events.length && events[idx][0] == day)
                pq.offer(events[idx++][1]);
            if(!pq.isEmpty()) {
                int pp = pq.poll();
                res++;
            }
        }
        return res;
    }
}
```

### [1909. Remove One Element to Make the Array Strictly Increasing](https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing)
```java
class Solution {
    public boolean canBeIncreasing(int[] nums) {
        int max = nums[0];
        boolean one = false;
        for(int i = 1; i < nums.length; i++) {
            if (nums[i] <= max) {
                if (one)
                    return false;
                one = true;
                if (i == 1 || nums[i] > nums[i - 2])
                    max = nums[i];
                else
                    max = nums[i - 1];
            } else
                max = nums[i];
        }
        return true;
    }
}
```

```java
class Solution {
    public boolean canBeIncreasing(int[] nums) {
        Stack<Integer> stack = new Stack<>();
        boolean one = false;
        for(int n : nums) {
            if (stack.isEmpty() || stack.peek() < n)
                stack.push(n);
            else {
                if (one)
                    return false;
                one = true;
                int prev = stack.pop();
                if (stack.isEmpty() || n > stack.peek())
                    stack.push(n);
                else {
                    stack.push(prev);
                }
            }
        }
        return true;
    }
}
```

### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
```java
class Solution {
    public int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE;
        int res = 0;
        for(int p  : prices) {
            min = Math.min(min, p);
            res = Math.max(res, p - min);
        }
        return res;
    }
}
```

### [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)
```java
class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        for(int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                res += prices[i] - prices[i - 1];
        }
        return res;
    }
}
```

### [2091. Removing Minimum and Maximum From Array](https://leetcode.com/problems/removing-minimum-and-maximum-from-array)
```java
class Solution {
    public int minimumDeletions(int[] nums) {
        int min = 0, max = 0;
        for(int i = 0; i < nums.length; i++) {
            if (nums[i] < nums[min])
                min = i;
            if (nums[i] > nums[max])
                max = i;
        }

        int front = Math.max(min, max) + 1;
        int back = nums.length - Math.min(min, max);

        int bigger = Math.max(min, max);
        int smaller = Math.min(min, max);
        int both = smaller + 1 + nums.length - bigger;

        return Math.min(both, Math.min(front, back));
    }
}
```

### [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)
```java
class Solution {
    public int reverse(int x) {
        boolean isNeg = x < 0 ? true : false;
        x = Math.abs(x);
        int rev = 0;
        while(x != 0) {
            int digit = x % 10;
            x = x / 10;
            if (rev > Integer.MAX_VALUE / 10 || rev < Integer.MIN_VALUE / 10)
                return 0;
            rev = rev * 10 + digit;
        }


        return isNeg ? -rev : rev;
    }
}
```

https://leetcode.com/problems/number-of-people-aware-of-a-secret/
```java
class Solution {
    public int peopleAwareOfSecret(int n, int delay, int forget) {
        long dp[] = new long[n + 1], mod = (long)1e9 + 7, share = 0, res = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; ++i)
            dp[i] = share = (share + dp[Math.max(i - delay, 0)] - dp[Math.max(i - forget, 0)] + mod) % mod;
        for (int i = n - forget + 1; i <= n; ++i)
            res = (res + dp[i]) % mod;
        return (int)res;
    }
}
```


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

https://leetcode.com/problems/maximum-subarray

https://leetcode.com/problems/maximum-width-of-binary-tree

https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful

https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

https://leetcode.com/problems/minimum-deletions-to-make-string-k-special

https://leetcode.com/problems/number-of-wonderful-substrings

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

https://leetcode.com/problems/repeated-substring-pattern

https://leetcode.com/problems/reveal-cards-in-increasing-order

https://leetcode.com/problems/reverse-nodes-in-k-group

https://leetcode.com/problems/rotate-array

https://leetcode.com/problems/split-array-into-consecutive-subsequences

https://leetcode.com/problems/subarray-sum-equals-k

https://leetcode.com/problems/subarray-sums-divisible-by-k

https://leetcode.com/problems/diagonal-traverse/

