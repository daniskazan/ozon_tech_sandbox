from collections import namedtuple
from enum import Enum
from typing import List, Tuple
from itertools import groupby
from collections import Counter
from functools import lru_cache

class ReportStatus(Enum):
    yes = "YES"
    no = "NO"


TestCase = namedtuple("TestCase", ["n", "report"])


def prepare_test_cases() -> List[TestCase]:
    test_cases: List[TestCase] = []
    case_count = int(input())

    for _ in range(case_count):
        n = int(input())
        report = [int(x) for x in input().split(maxsplit=n-1)]
        test_cases.append(TestCase(n=n, report=report))
    return test_cases

def lst_of_sequences(lst: List[int]) -> Tuple[Tuple[int]]:
    sequences = tuple(tuple(g) for _, g in groupby(lst))
    return sequences


@lru_cache(maxsize=1024)
def check(seqs: Tuple[Tuple[int]]) -> List[List[int]]:
    for seq in seqs:
        idx = seqs.index(seq) + 1
        tail = seqs[idx:]
        other_part = {element for tupl in tail for element in (tupl if isinstance(tupl, tuple) else (tupl,))}
        curr = seq[0]
        if curr in other_part:
            return True
    return False


def main(test_cases: List[TestCase]):
    for test in test_cases:
        data = lst_of_sequences(test.report)
        if check(data):
            print("NO")
        else:
            print("YES")



if __name__ == '__main__':
    tests = prepare_test_cases()
    main(test_cases=tests)
