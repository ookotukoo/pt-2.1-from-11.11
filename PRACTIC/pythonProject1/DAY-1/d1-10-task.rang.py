rank = 'рядовойсержантстаршинапрапорщиклейтенанткапитанмайорподполковникполковник'

lst_in = ('''
Иванов=лейтенант
Никита=полковник
Петров=прапорщик
Сидоров=капитан
Егоров=лейтенант
Смирнов=рядовой

'''.strip().splitlines())


lst_in = [user.split('=') for user in lst_in]

lst_in = sorted(lst_in, key=lambda x: rank.index(x[1]))


print(*lst_in, sep='\n')