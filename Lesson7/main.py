from counter import Counter
#iter1 = iter([1,2,3,4,5,6,7,8,9,10])
'''
for i in iter1:
    print(i)
'''
'''
try:
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
except StopIteration:
    pass
'''
#iter0 = Counter(15, 21)
'''
for _ in iter0:
    print(iter0.__str__())
'''
'''
while(True):
    try:
        print(iter0.__str__())
        iter0.__next__()
    except StopIteration:
        break
'''
'''
#2_generator
from generator import Generator
generator = Generator(5)
res = generator.Pow(3)
for i in res:
    print(i)
'''
#3 call objects
'''
from generator import Generator
generator = Generator(10)
print(generator.__str__())
print(generator(15))
print(generator.Number)
'''
#4 decorator
from decorator import Checker
checker = Checker()
#calculate = checker.Check(checker.Calculate)
#calculate("'h'*2")
val1 = input("Enter val1: ")
val2 = input("Enter val2: ")
operation = input("Enter operation: ")
checker.Calculate(f"{val1}{operation}{val2}")
