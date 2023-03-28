faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53

faturamento_total = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

percentual_sp = (faturamento_sp/faturamento_total) * 100
percentual_rj = (faturamento_rj/faturamento_total) * 100
percentual_mg = (faturamento_mg/faturamento_total) * 100
percentual_es = (faturamento_es/faturamento_total) * 100
percentual_outros = (faturamento_outros/faturamento_total) * 100

print("O percentual do estado SP foi: {:.2f}%".format(percentual_sp))
print("O percentual do estado RJ foi: {:.2f}%".format(percentual_rj))
print("O percentual do estado MG foi: {:.2f}%".format(percentual_mg))
print("O percentual do estado ES foi: {:.2f}%".format(percentual_es))
print("O percentual do estado OUTROS foi: {:.2f}%".format(percentual_outros))
