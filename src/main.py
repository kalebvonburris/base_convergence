import bases as bases

n = 150
base = 40
neg = bases.dec_to_base(n, -base)
pos = bases.dec_to_base(n, base)
print(f'Base +{base}: {pos}\nBase -{base}: {neg}')