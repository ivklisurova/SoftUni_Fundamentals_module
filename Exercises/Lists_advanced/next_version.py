current_version = list(map(int, input().split('.')))


def solve(curr_ver_list):
    next_version = curr_ver_list
    next_version[2] = next_version[2] + 1

    if next_version[2] > 9:
        next_version[1] += 1
        next_version[2] = 0
        if next_version[1] > 9:
            next_version[1] = 0
            next_version[0] += 1
    return next_version


def output(next_ver_list):
    print(*next_ver_list, sep='.')


output(solve(current_version))