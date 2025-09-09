def maior(*num):
    print(f'Valores: {", ".join(map(str, num))} \nForam informados {len(num)} valores ao todo.')
    print(f'O maior valor encontrado foi: {max(num)}.\n')


maior(2, 9, 4, 5, 7, 1)

maior(4, 7, 0)

maior(1, 2)

maior(0)