"""
my task from the raelX Unlocking Information Security lesson in the course i participated in.
"""
import sys  # ignore
import time

sys.path.insert(0, '.')  # ignore

real_password = "2687"


def check_password(password):  # Don't change it
    """
    given method.
    my mission is to crack it
    :param password:
    :return:
    """
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.2)  # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True


def crack_password():
    """
    using time attack to crack the password
    :return:
    """
    check = False
    password = "0000"
    for pos in range(0, 4):
        for digit in range(0, 10):
            password = list(password)
            password[pos] = str(digit)
            password = "".join(password)
            start = time.time()
            check_password(password)
            end = time.time()
            duration = end - start
            if pos == 3:
                if not check:
                    check = check_password(password)
            if check:
                print(password)
                return password
            if pos != 3 and duration > 0.22 * (pos + 1):
                break
    return password


def main():
    print(crack_password())


if __name__ == '__main__':
    main()
