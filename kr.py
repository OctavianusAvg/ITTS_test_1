'''
2.Вводиться дійсне число R. Обчислити і вивести довжину окружності, площу кола і об'єм кулі одного радіуса R.
(0 ≤ R ≤ 100)
'''
while True:
    R = float(input('Введіть R: '))
    if 0 <= R <= 100:
        break

from math import pi

print(f'Довжина кола: {2 * pi * R}')
print(f'Площа кола: {pi * R * R}')
print(f'Об\'єм кулі: {(4 / 3) * (pi * R ** 3)}')
