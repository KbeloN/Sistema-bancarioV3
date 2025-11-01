from datetime import datetime, timedelta

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime('%d/%m/%Y, %H:%M:%S'),
                "data_dt": datetime.now()
            }
        )

    def gerar_historico(self, tipo_transacao=None):
        for transacao in self.transacoes:
            if tipo_transacao is None or transacao["tipo"] == tipo_transacao.__name__:
                yield transacao

    def saques_do_dia(self):
        from .transacao import Saque

        saques_diarios = 0
        datetime_now = datetime.now()

        for transacao in self.transacoes:
            data_transacao = transacao['data_dt']
            resultado: timedelta = datetime_now - data_transacao
            
            if resultado.days == 0 and transacao['tipo'] == Saque.__name__:
                saques_diarios +=1
        
        return saques_diarios