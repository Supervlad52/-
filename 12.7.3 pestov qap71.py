money = int(input( "сумма под процент:" ))
per_cent = {'TKB': 5.6, 'CKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
newlist = list(per_cent.values())
print(per_cent.values())
deposit = [i * (money / 100) for i in newlist]
print(deposit)
max_element = max(deposit)
print("Max element of a list: ", max_element)
