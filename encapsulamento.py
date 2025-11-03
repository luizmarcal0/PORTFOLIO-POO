class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial
    
    @property
    def saldo(self):
        """Este método 'get' permite ler o saldo."""
        if self.__saldo < 0:
            return 0
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_valor):
        """Este método 'set' valida antes de alterar."""
        if novo_valor < 0:
            print("Erro: O saldo não pode ser negativo.")
        else:
            self.__saldo = novo_valor

conta = ContaBancaria(100)

print(f"Saldo atual: R${conta.saldo}")

conta.saldo = 150
print(f"Novo saldo: R${conta.saldo}")

conta.saldo = -50
print(f"Saldo após tentativa negativa: R${conta.saldo}")
