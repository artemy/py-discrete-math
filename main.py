#!/usr/bin/env python3
# Author: Artem Makarov

MEMBERS_X = range(1, 6)
MEMBERS_Y = range(1, 6)


def create_set(members_x, members_y, function):
    return [[x, y] for x in members_x for y in members_y if function(x, y)]


def create_tau():
    return create_set(MEMBERS_X, MEMBERS_Y, lambda x, y: x + y < 5)


def create_rho():
    return create_set(MEMBERS_X, MEMBERS_Y, lambda x, y: abs((3 - x) * (3 - y)) <= 1)


def sort(set):
    result = set.copy()
    result.sort()
    return result


def unique(set):
    result = []
    for [x, y] in set:
        if [x, y] not in result:
            result.append([x, y])
    return result


# set composition
def compose(set1, set2):
    return sort(unique([[x1, y2] for [x1, y1] in set1 for [x2, y2] in set2 if y1 == x2]))


# set inverse relation
def inverse(set):
    return sort(unique([[y, x] for [x, y] in set]))


# set transitive closure
def transitive(set):
    return compose(set, set)


def set_as_matrix(set):
    dummy = ''
    for x in MEMBERS_X:
        for y in MEMBERS_Y:
            dummy = dummy + ('1' if [x, y] in set else '0')
        dummy = dummy + '\n'
    return dummy


def print_set_and_matrix(set):
    print(set)
    print(set_as_matrix(set))


def main():  # pragma: no cover
    rho = create_rho()
    print('Set Rho')
    print_set_and_matrix(rho)

    tau = create_tau()
    print('Set Tau')
    print_set_and_matrix(tau)

    print('Composition of Rho and Tau')
    print_set_and_matrix(compose(rho, tau))

    print('Inverse relation of Rho')
    print_set_and_matrix(inverse(rho))

    print('Inverse relation of Tau')
    print_set_and_matrix(inverse(tau))

    print('Composition of both inverse Rho and Tau')
    print_set_and_matrix(compose(inverse(rho), inverse(tau)))

    print('Transitive closure of Rho')
    print_set_and_matrix(transitive(rho))

    print('Transitive closure of Tau')
    print_set_and_matrix(transitive(tau))

    print('Transitive composition of Rho and Tau')
    print_set_and_matrix(transitive(compose(rho, tau)))


if __name__ == '__main__':  # pragma: no cover
    main()
