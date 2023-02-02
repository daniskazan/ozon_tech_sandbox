from collections import defaultdict
from typing import List, Tuple


def recommend_friends(n: int, friendships: List[Tuple], user: int):
    """
    :param n the number of users in the network.
    :param friendships: a list of tuples representing the friendship relationships between users.
    :param user: the id of the user for whom the list of possible friends needs to be calculated.
    """
    graph = defaultdict(list)

    for x, y in friendships:
        graph[x].append(y)
        graph[y].append(x)

    possible_friends = []
    max_mutual_friends = -1
    for i in range(1, n+1):
        if len(possible_friends) > 5:
            continue
        if i == user or i in graph[user]:
            continue

        mutual_friends = len(set(graph[user]).intersection(set(graph[i])))
        if mutual_friends and mutual_friends > max_mutual_friends:
            max_mutual_friends = mutual_friends
            possible_friends = [i]
        elif mutual_friends == max_mutual_friends:
            possible_friends.append(i)
    return possible_friends


def get_friends_map() -> Tuple[int, List[Tuple[int, int]]]:
    users_count, pairs_count = [int(x) for x in input().split()]
    friends_map = []
    for _ in range(pairs_count):
        self_user, other_user = [int(x) for x in input().split()]
        friendship = (self_user, other_user)
        friends_map.append(friendship)
    return users_count, friends_map


def main():
    n, friendships = get_friends_map()
    for user in range(1, n + 1):
        friends = recommend_friends(n, friendships, user)
        if friends:
            print(*friends)
        else:
            print(0)


if __name__ == '__main__':
    main()