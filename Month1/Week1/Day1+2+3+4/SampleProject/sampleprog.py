"""This is a simple program to practice on classes and
inheritence.
"""


class Bankaccount:
    def __init__(self):
        self.balance = 0

    def addAmount(self, amt):
        self.balance += amt
        return self.balance


class MinBalAccount(Bankaccount):
    minbal = 50

    def __init__(self):
        Bankaccount.__init__(self)
        # self.minbal = 50

    def withdraw(self, amt):
        if (self.balance-amt < self.minbal):
            print 'Cannot withdraw amount.'
        else:
            # self.balance -= amt
            print 'balance here: ', self.balance
            bal = self.balance
            rem = bal - amt
            self.balance -= amt
            print 'we\'re here'
            print 'rem = ', rem
            print 'withdrawn ammount %f and remaining ammount is %f' % (amt,
                                                                        rem)
            # return self.balance


def main():
    myacc = Bankaccount()
    myacc.addAmount(50)
    print 'My account balance is %d' % myacc.balance

    myacc.addAmount(50)
    print "My account balance is %d" % myacc.balance

    myminacc = MinBalAccount()
    print 'My min bal acc balance is %d' % myminacc.balance

    myminacc.addAmount(75)

    print 'My min bal acc balance is %d' % myminacc.balance

    myminacc.addAmount(100)

    print 'My min bal acc balance is %d' % myminacc.balance

    myminacc.withdraw(30)
    myminacc.withdraw(30)
    myminacc.withdraw(20)
    myminacc.withdraw(50)
    myminacc.withdraw(10)


if __name__ == '__main__':
    main()
