from math import gcd


def p2c(p: str) -> tuple[int, int]:
    """
    Функция переводит бесконечную периодическую дробь в обыкновенную.
    :param p: десятичная периодическая дробь в виде строки (например 1.5(3))
    :return: числитель, знаменатель
    """
    a, tmp = p.split('.')
    b, c = tmp[:-1].split('(')
    z = int('9'*len(c) + '0'*len(b))
    c = int(a + b + c) - int(a + b)
    g = gcd(c, z)
    return c // g, z // g


if __name__ == '__main__':
    c, z = p2c(input('>'))
    print(f'{c}/{z} = {c/z}')


