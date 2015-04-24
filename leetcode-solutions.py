import operator
# Solutions to problems at https://oj.leetcode.com/problemset/algorithms/
class LeetSolutions:

    def reverseBits(self, n):
        n = bin(n)[2:]
        pad = 32 - len(n)
        n = "0"*pad + n
        return int(n[::-1], 2)

    # 189 - https://oj.leetcode.com/problems/rotate-array/
    # Rotate an array of n elements (in place) to the right by k steps.
    # For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]
    
    def rotate(self, nums, k):
        k = k % len(nums)
        pivot = len(nums) - k
        left = reversed(nums[:pivot])
        right = reversed(nums[pivot:])
        nums = (left + right)
        nums.reverse()
        return

    
    # 187 - https://oj.leetcode.com/problems/repeated-dna-sequences/
    # All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for 
    # example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
    # Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule
    
    def findRepeatedDnaSequences(self, s, seqSize = 10):
        repeated = []
        sequences = {}
        for i in range(len(s)):
            sequence = s[i:i+seqSize]
            if (sequence not in repeated) and (sequence in sequences):
                repeated.append(sequence)
            sequences[sequence] = 1
        return repeated


    # 179 - https://oj.leetcode.com/problems/largest-number/
    # Given a list of non negative integers, arrange them such that they form the largest number.
    # For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
    # Note: The result may be very large, so you need to return a string instead of an integer.

    def largestNumber(self, num):
        def compare(num1, num2):
            test1 = num1 + num2
            test2 = num2 + num1
            return cmp(test1, test2)
        num = reversed(sorted(map(str, num), cmp=compare))
        if num[0] == "0":
            return "0"
        else: 
            return "".join(num)


    # 173 - https://oj.leetcode.com/problems/binary-search-tree-iterator/
    # Implement an iterator over a binary search tree (BST). 
    # Your iterator will be initialized with the root node of a BST.
    # Implement the methods next() and hasNext() to return the node values in ascending order

    # Definition for a  binary tree node
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class BSTIterator:
        # @param root, a binary search tree's root node
        def __init__(self, root):
            self.orderedValues = []
            def collectValsInOrder(rt, vals):
                if rt:
                    if rt.right:
                        collectValsInOrder(rt.right, vals)
                    vals.append(rt.val)
                    if rt.left:
                        collectValsInOrder(rt.left, vals)
            collectValsInOrder(root, self.orderedValues)
                    

        # @return a boolean, whether we have a next smallest number
        def hasNext(self):
            return len(self.orderedValues) > 0
            

        # @return an integer, the next smallest number
        def next(self):
            return self.orderedValues.pop()


    # 172 - https://oj.leetcode.com/problems/factorial-trailing-zeroes/
    # Given an integer n, return the number of trailing zeroes in n!.

    def trailingZeroes(self, n):
        if n/5 == 0:
            return 0
        else:
            return n/5 + self.trailingZeroes(n/5)


    # 171 - https://oj.leetcode.com/problems/excel-sheet-column-number/
    # Given a column title as appear in an Excel sheet, return its corresponding column number.
    # For Example: "A" -> 1, "B" -> 2, ... , "Z" -> 26, "AA" -> 27, "AB" -> 28
    
    def titleToNumber(self, s):
        s, length, total = s.lower(), len(s), 0 
        for i in range(0, length):
            total += (ord(s[i]) - 96) * (26 ** (length - i - 1))
        return total



    def majorityElement(self, num):
        elements, majority = {None: 0}, None
        for element in num:
            if element in elements:
                elements[element] += 1
            else:
                elements[element] = 1
            if elements[element] > elements[majority]:
                majority = element
                
        return majority


    # 168 - https://oj.leetcode.com/problems/excel-sheet-column-title/
    # Given a positive integer, return its corresponding column title as appear in an Excel sheet
    # Reverse of problem 171

    def convertToTitle(self, num):
        s = ""
        while num:
            s = chr((num - 1) % 26 + ord('A')) + s
            num = (num - 1) / 26
        return s

    def convertToTitleRecursive(self, num):
        if num == 0: return ""
        else: return self.convertToTitleRecursive((num-1)/26) + chr((num - 1) % 26 + ord('A'))


    # 166 - https://oj.leetcode.com/problems/fraction-to-recurring-decimal/
    # Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
    # If the fractional part is repeating, enclose the repeating part in parentheses.

    def fractionToDecimal(self, numerator, denominator):
        neg = False
        if numerator * denominator < 0:
            neg = True
        numerator, denominator = abs(numerator), abs(denominator)
        v = numerator // denominator
        numerator = 10 * (numerator - v * denominator)
        answer = str(v)
        
        if numerator != 0:
            answer += '.' 
            states = {}
            while numerator > 0:
                repeat_index = states.get(numerator, None)
                
                if repeat_index != None:
                   answer = answer[:repeat_index] + '(' + answer[repeat_index:] + ')'
                   break
                states[numerator] = len(answer)
                v = numerator // denominator
                answer += str(v)
                numerator = 10 * (numerator - v * denominator)        
        return '-' + answer if neg else answer


    # 165 - https://oj.leetcode.com/problems/compare-version-numbers/
    # Compare two version numbers version1 and version2.
    # If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
    # You may assume that the version strings are non-empty and contain only digits and the . character.
    
    def compareVersion(self, version1, version2):
        version1 = map(int, version1.split('.'))
        version2 = map(int, version2.split('.'))
        for i in range(min(len(version1), len(version2))):
            if version1[i] > version2[i]: return 1
            elif version1[i] < version2[i]: return -1
            
        if len(version1) > len(version2) and version1[len(version2)] != 0: return 1
        elif len(version1) < len(version2) and version2[len(version1)] != 0: return -1
        else: return 0


    # 162 - https://oj.leetcode.com/problems/find-peak-element/
    # A peak element is an element that is greater than its neighbors.
    # Given an input array where num[i] != num[i+1], find a peak element and return its index.
    # The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

    def findPeakElement(self, num):
        for i in range(len(num)-1):
            if num[i] > num[i+1]: return i
        return len(num)-1


    # 160 - https://oj.leetcode.com/problems/intersection-of-two-linked-lists/
    # Write a program to find the node at which the intersection of two singly linked lists begins.
    # For example, the following two linked lists:
    #
    # A:          a1 -> a2
    #                      ->
    #                         c1 -> c2 -> c3
    #                      ->           
    # B:     b1 -> b2 -> b3
    # begin to intersect at node c1.
    #
    # If the two linked lists have no intersection at all, return null.
    # The linked lists must retain their original structure after the function returns.
    # You may assume there are no cycles anywhere in the entire linked structure.
    # Your code should preferably run in O(n) time and use only O(1) memory
    
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        # @param two ListNodes
        # @return the intersected ListNode
        def getIntersectionNode(self, headA, headB):
            def listlen(head):
                count = 0
                while head:
                    count += 1
                    head = head.next
                return count
                
            lenA = listlen(headA)
            lenB = listlen(headB)
            longer = headA
            shorter = headB
            dif = 0
            if lenA >= lenB:
                dif = lenA - lenB
            else:
                longer = headB
                shorter = headA
                dif = lenB - lenA
            for i in range(dif):
                longer = longer.next
            for i in range(min(lenA, lenB)):
                if longer.val == shorter.val:
                    return longer
                longer = longer.next
                shorter = shorter.next
            return None


    # 155 - https://oj.leetcode.com/problems/min-stack/
    # Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    # push(x) -- Push element x onto stack.
    # pop() -- Removes the element on top of the stack.
    # top() -- Get the top element.
    # getMin() -- Retrieve the minimum element in the stack.

    class MinStack:
    
        def __init__(self):
            self.data = []
            self.mins = []
        
        # @param x, an integer
        # @return an integer
        def push(self, x):
            if len(self.data) == 0:
                self.mins.append(x)
            elif x <= self.mins[-1]:
                self.mins.append(x)
            self.data.append(x)
            

        # @return nothing
        def pop(self):
            if len(self.data) != 0:
                val = self.data.pop()
                if val == self.mins[-1]:
                    self.mins.pop()
                return val
            

        # @return an integer
        def top(self):
            if len(self.data) != 0: return self.data[-1] 

        # @return an integer
        def getMin(self):
            if len(self.data) != 0: return self.mins[-1]


    # 153 & 154 - https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
    # Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    # (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    # Find the minimum element.

    def findMin(self, num):
        left = 0
        right = len(num)-1
        
        while left < right:
            mid = (left + right) / 2
            if num[left] < num[right]: return num[left]
            elif num[left] < num[mid]: left = mid + 1
            elif num[right] > num[mid]: right = mid
            else:
                if num[mid] != num[right]: left = mid + 1
                else:
                    left += 1
                    right -= 1
        return num[right]


    # 151 - https://oj.leetcode.com/problems/reverse-words-in-a-string/    
    # Given an input string, reverse the string word by word.
    # For example, Given s = "the sky is blue", return "blue is sky the"
    def reverseWords(self, s):
        s = reversed(s.split())
        return " ".join(s)


    # 150 - https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/
    # Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    # Valid operators are +, -, *, /. Each operand may be an integer or another expression.
    # Some examples:
    #   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
    #   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6 
    
    def evalRPN(self, tokens):
        ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        stack = []
        for token in tokens:
            if token in ops:
                right = stack.pop()
                left = stack.pop()
                neg = False
                if token == "/" and right * left < 0: 
                    neg = True
                    right = abs(right)
                    left = abs(left)
                stack.append(-ops[token](left, right) if neg else ops[token](left, right))
            else: stack.append(int(token))
        return stack.pop()

    

solutions = LeetSolutions()
print solutions.reverseBits(1)



