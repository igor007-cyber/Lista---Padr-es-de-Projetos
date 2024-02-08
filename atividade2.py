class ILog:
    def registrar(self, msg):
        pass


class LogArquivo(ILog):
    def registrar(self, msg):
        print("Registrando em arquivo:", msg)


class LogConsole(ILog):
    def registrar(self, msg):
        print("Registrando no console:", msg)


class LogBancoDeDados(ILog):
    def registrar(self, msg):
        print("Registrando no banco de dados:", msg)


class LogFactory:
    @staticmethod
    def criar_log(tipo):
        tipo = tipo.lower()
        if tipo == "arquivo":
            return LogArquivo()
        elif tipo == "console":
            return LogConsole()
        elif tipo == "banco":
            return LogBancoDeDados()
        else:
            raise ValueError("Tipo de log desconhecido: " + tipo)


if __name__ == "__main__":
    log_arquivo = LogFactory.criar_log("arquivo")
    log_console = LogFactory.criar_log("console")
    log_banco = LogFactory.criar_log("banco")

    log_arquivo.registrar("Mensagem de log em arquivo")
    log_console.registrar("Mensagem de log no console")
    log_banco.registrar("Mensagem de log no banco de dados")
