class main:
   ...

from Cliente import Cliente
from Conta import Conta

c1 = Cliente('Nando', '986115281')
conta = Conta('Nando', 1222, 50)

conta.deposita(100)
conta.saque(70)
conta.extrato()