from typing import Dict


def get_friends_map() -> Dict[int, list]:
    users_count, pairs_count = [int(x) for x in input().split()]
    friends_map = {k: [] for k in range(1, users_count + 1)}
    for _ in range(pairs_count):
        self_user, other_user = [int(x) for x in input().split()]
        friends_map[self_user] += [other_user]
        friends_map[other_user] += [self_user]
    return friends_map


def get_possible_friends(mapping: Dict):
    uids = list(mapping.keys())
    # print(uids)
    possible_friends = {user_id: {0} for user_id in uids}
    for uid in uids:
        max_mutual_friends_amount = -1
        current_user_friends = mapping.get(uid)
        other_people = [people for people in uids if people not in current_user_friends and people != uid]

        # print(f"OTHER PEOPLE {other_people}")
        # print()

        if max_mutual_friends_amount > 5:
            continue

        for other in other_people:
            other_user_friends = mapping.get(other)
            mutual_friends = tuple((set(current_user_friends) & set(other_user_friends)))
            # print(f"USER_ID = {uid}, his friends is {current_user_friends}")
            # print(f"OTHER_USER_ID = {other}, his friends is {other_user_friends}")
            # print(f"THEIR MUTUAL FRIENDS ARE {mutual_friends}")
            # print("=============")
            if all([mutual_friends, len(mutual_friends) > max_mutual_friends_amount]):
                # удалить всех из списка возможных друзей
                max_mutual_friends_amount = len(mutual_friends)
                possible_friends[uid] = {other}
            elif len(mutual_friends) == max_mutual_friends_amount:
                possible_friends[uid].add(other)

    return possible_friends


def main():
    friends_map = get_friends_map()
    # print(friends_map)
    possible_friends = get_possible_friends(friends_map)
    for v in possible_friends.values():
        print(*sorted(v))


if __name__ == '__main__':
    main()