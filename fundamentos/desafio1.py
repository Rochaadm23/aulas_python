# Desafio operadores lógicos

trabalho_terca = True
trabalho_quinta = True

"""

 - Confirmando os 2: TV 50 + Sorvete
 - Confirmando apenas 1: TV 32 + Sorvete
 - Nenhum confirmado: Fica em casa

"""
tv_50 = trabalho_terca and trabalho_quinta
soverte = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
maisaudavel = not soverte

print("Tv50={}, Tv32={}, Sorvete={}, Saudável={}".format(tv_50, tv_32, soverte, maisaudavel))
