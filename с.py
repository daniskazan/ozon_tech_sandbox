from collections import namedtuple
from typing import List


Developer = namedtuple("Developer", ["id", "skill"])

def main():
    case_count = int(input())
    for _ in range(case_count):
        n = int(input())
        developers_ids = list(range(1, n + 1))
        skills_degree = [int(x) for x in input().split(maxsplit=n-1)]

        developers: List[Developer] = list(map(Developer, developers_ids, skills_degree))
        teams = []
        while developers != []:
            first = developers.pop(0)
            teammate = min(developers, key=lambda d: abs(first.skill - d.skill))
            teams.append((first.id, teammate.id))
            developers.remove(teammate)
        for t in teams:
            print(" ".join(map(str, t)))
        print()



if __name__ == '__main__':
    main()