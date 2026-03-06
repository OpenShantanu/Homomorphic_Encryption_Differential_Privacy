import tenseal as ts

context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60,40,40,60]
)

context.global_scale = 2**40
context.generate_galois_keys()

salaries = ts.CKKSVector(context, [30000, 40000, 50000])

encrypted_sum = salaries.sum()
encrypted_avg = encrypted_sum * (1/3)

print(encrypted_avg.decrypt())
