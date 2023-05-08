class Conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self._num = numero
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    '''
    Em Python, não é considerada uma boa prática criar uma classe e,
    logo em seguida, adicionar propriedades (property) para todos os atributos.
    A função Property deve ser utilizada somente se você precisar da funcionalidade de transformar ou verificar um atributo
    quando ele é atribuído ou lido.
    '''

    @property
    def saldo(self, saldo):
        if saldo < 0 :
            print('O Saldo não pode ser nergativo!!')

        else :
            self._saldo = saldo

    
    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print('Saque realizado com sucesso.')
        
        else:
            print('Não foi possível sacar :(')

    def deposita(self, valor):
        self._saldo += valor

    def extrato(self):
        print('Nome :', self._titular, 'Número :', self._num ,'Saldo Atual :', self._saldo)