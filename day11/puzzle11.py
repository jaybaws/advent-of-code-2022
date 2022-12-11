import math

class Monkey:

    def __init__(self, items:list[int], operation:str, modulo:int, recipient_false:str, recipient_true:str):
        self.__items = items
        self.__operation = operation
        self.__modulo = modulo
        self.__recipient_false = recipient_false
        self.__recipient_true = recipient_true
        self.__inspections = 0

    def divisor(self) -> int:
        return self.__modulo

    def receiveItem(self, item: int) -> None:
        self.__items.append(item)

    def playRound(self, peers:dict, divisor:int, limiter:int) -> None:
        for item in self.__items:
            self.__inspections += 1
            new = eval(self.__operation, {}, { "old": int(item) })
            new //= divisor
            new = new % limiter
            divisible = new % self.__modulo == 0
            recipient = self.__recipient_true if divisible else self.__recipient_false
            recipient_monkey = peers[recipient]
            recipient_monkey.receiveItem(new)
        self.__items.clear()
 
    def inspections(self):
        return self.__inspections

monkeys = dict()

def load() -> None:
    with open('input.txt', 'r') as f:
        chunks = f.read().split("\n\n")
        for chunk in chunks:
            parts = chunk.split("\n")
            name = parts[0][-2]
            items = parts[1][18:].split(", ")
            operation = parts[2][19:]
            modulo = int(parts[3][21:])
            recipient_true = str(parts[4][-1])
            recipient_false = str(parts[5][-1])
            m = Monkey(items, operation, modulo, recipient_false, recipient_true)
            monkeys[name] = m


def answer(rounds:int, divisor:int) -> int:
    limiter = math.prod([monkeys[name].divisor() for name in monkeys])
    for _ in range(1, rounds + 1):
        for name in monkeys:
            monkey = monkeys[name]
            monkey.playRound(monkeys, divisor, limiter)

    inspections = sorted([monkeys[name].inspections() for name in monkeys], reverse=True)[:2]
    return math.prod(inspections)

def answer1() -> int:
    return answer(20, 3)

def answer2() -> int:
    return answer(10_000, 1)


load()
a1 = answer1()

load()
a2 = answer2()

print(f"""
    Answer 1: {a1}
    Answer 2: {a2}
""")

# *** Thoughts directly after completion:
# - Happy to get the input parsing done relatively quickly
#   - Thought at first to 'hard-code' my input as a dict to avoid parsing and define functions for the math operations
#     -> Learnt soon enough that Python can dynamically execute code using eval() and exec()
#        -> Struggled with exec(). Got that working in static code, but not part of a class method. Still no clue why...
#           -> Reverted to using eval() which did the trick.
# - Understood pretty quickly that this was best solved procedurally.
# - Thought about NumPy, but realized this wasn't the moment :)
# - Struggled quite a bit to find cause+solution to app performance degradation during part 2.
# - Could have done better dependency-inversion by passing list[monkeys] into the functions, but didn't care enough :)
# - Could have done better type-hinting by importin List from types and declaring List[Monkey], but didn't care enough :)

# *** Thoughts after seeing other people's solutions:
# - Array could have also worked. No real need for OOP; but didn't see how at the time.
# - There were ways to compute answer 2 without having to load the input file again. 

# *** Learnings:
# - dynamic code execution using eval() and exec()
# - private instance variables
# - integer notation 10_000 for enhanced readability