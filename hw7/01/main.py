def slog(chant):
    st = chant.lower().split()
    def f(x): return sum(1 for i in x if i in 'аеёиоуыэюя')
    tmp = f(st[0])
    if all([f(i) == tmp for i in st]):
        return 'Парам пам-пам'
    return 'Пам парам'


print(slog("Раз-два-Три"))

print(slog("Нет Дада"))
