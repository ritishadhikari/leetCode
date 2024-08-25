class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # nums (list of lists of int): all the numbers in the input
        # opts (list of lambda functions): all the operator in the input
        nums, opts = parse(input)

        # A 3D array. See the definition of d.
        arr = [nums]

        # d(i,j) = arr[j-i][i], all the possible values obtained from i-th number to j-th number
        d = lambda start, end: arr[end - start][start]

        # Fill d in increasing order of num_operands=(j-i)
        for num_operands in range(2, len(nums) + 1):
            new_lv = []
            for start in range(0, len(nums) - num_operands + 1):
                # values (list): Cartesian product of d(start,split) and d(split+1,end)
                #     for all possible splits from start-th operand to end-th operand.
                values = []
                for split in range(start, start + num_operands - 1):
                    for a in d(start, split):
                        for b in d(split + 1, start + num_operands - 1):
                            values.append(opts[split](a, b))
                new_lv.append(values)
            arr.append(new_lv)

        return arr[-1][0]


def parse(input):
    num = 0
    nums = []
    opts = []
    for c in input:
        if c.isdigit():
            num = num * 10 + int(c)
        else:
            nums.append([num])
            opts.append(char2lambda(c))
            num = 0
    nums.append([num])
    return nums, opts


def char2lambda(c):
    if c == '+':
        return lambda a, b: a + b
    elif c == '-':
        return lambda a, b: a - b
    elif c == '*':
        return lambda a, b: a * b
    

if __name__=="__main__":
    expression = "2*3-4*5"
    print(Solution().diffWaysToCompute(input=expression))
    
