"""This Program weites a python class to find three elments that sum to zero
form a set of n real numbers.
"""


class SumZero:
    """class description will be given here."""

    newList = []

    def __init__(self, numlist):
        self.nums = numlist

    def giveNums(self):
        print 'input list is: %s' % self.nums
        n = len(self.nums)
        print 'length of our list = %s' % n
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                sum = self.nums[i]+self.nums[j]+self.nums[j+1]
                print 'sum here: %s' % sum
                if (sum == 0):
                    self.newList = [self.nums[i], self.nums[j], self.nums[j+1]]
        return self.newList


def main():
    myNums = SumZero([-1, 2, -1, 2, 3, -2])
    ans = myNums.giveNums()
    print 'This is our answer: %s' % ans


if __name__ == '__main__':
    main()
