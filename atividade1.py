class Configuracao:
    _instance = None

    def __init__(self, tema, idioma, tamanho_fonte):
        self.tema = tema
        self.idioma = idioma
        self.tamanho_fonte = tamanho_fonte

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls("claro", "português", 12)
        return cls._instance

    def get_tema(self):
        return self.tema

    def set_tema(self, tema):
        self.tema = tema

    def get_idioma(self):
        return self.idioma

    def set_idioma(self, idioma):
        self.idioma = idioma

    def get_tamanho_fonte(self):
        return self.tamanho_fonte

    def set_tamanho_fonte(self, tamanho_fonte):
        self.tamanho_fonte = tamanho_fonte


if __name__ == "__main__":
    configuracao = Configuracao.get_instance()

    print("Configurações Iniciais:")
    print("Tema:", configuracao.get_tema())
    print("Idioma:", configuracao.get_idioma())
    print("Tamanho da Fonte:", configuracao.get_tamanho_fonte())

    configuracao.set_tema("escuro")
    configuracao.set_idioma("inglês")
    configuracao.set_tamanho_fonte(14)

    print("\nConfigurações Alteradas:")
    print("Tema:", configuracao.get_tema())
    print("Idioma:", configuracao.get_idioma())
    print("Tamanho da Fonte:", configuracao.get_tamanho_fonte())

    nova_configuracao = Configuracao.get_instance()
    print("\nNova Configuração é a Mesma Instância?", configuracao is nova_configuracao)
