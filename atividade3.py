from abc import ABC, abstractmethod

# Interface para os produtos
class Botao(ABC):
    @abstractmethod
    def clicar(self):
        pass

class Janela(ABC):
    @abstractmethod
    def renderizar(self):
        pass

class Cursor(ABC):
    @abstractmethod
    def mover(self):
        pass

class Select(ABC):
    @abstractmethod
    def selecionar_opcao(self):
        pass

class Input(ABC):
    @abstractmethod
    def manipular_entrada(self):
        pass

# Fábrica abstrata
class UIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_janela(self) -> Janela:
        pass

    @abstractmethod
    def criar_cursor(self) -> Cursor:
        pass

    @abstractmethod
    def criar_select(self) -> Select:
        pass

    @abstractmethod
    def criar_input(self) -> Input:
        pass

# Fábrica concreta para Windows
class WindowsUIFactory(UIFactory):
    def criar_botao(self) -> Botao:
        return WindowsBotao()

    def criar_janela(self) -> Janela:
        return WindowsJanela()

    def criar_cursor(self) -> Cursor:
        return WindowsCursor()

    def criar_select(self) -> Select:
        return WindowsSelect()

    def criar_input(self) -> Input:
        return WindowsInput()

# Fábrica concreta para macOS
class MacOSUIFactory(UIFactory):
    def criar_botao(self) -> Botao:
        return MacOSBotao()

    def criar_janela(self) -> Janela:
        return MacOSJanela()

    def criar_cursor(self) -> Cursor:
        return MacOSCursor()

    def criar_select(self) -> Select:
        return MacOSSelect()

    def criar_input(self) -> Input:
        return MacOSInput()

# Implementações concretas para Windows
class WindowsBotao(Botao):
    def clicar(self):
        print("Botão do Windows clicado")

class WindowsJanela(Janela):
    def renderizar(self):
        print("Janela do Windows renderizada")

class WindowsCursor(Cursor):
    def mover(self):
        print("Cursor do Windows movido")

class WindowsSelect(Select):
    def selecionar_opcao(self):
        print("Opção selecionada no Windows")

class WindowsInput(Input):
    def manipular_entrada(self):
        print("Entrada manipulada no Windows")

# Implementações concretas para macOS
class MacOSBotao(Botao):
    def clicar(self):
        print("Botão do macOS clicado")

class MacOSJanela(Janela):
    def renderizar(self):
        print("Janela do macOS renderizada")

class MacOSCursor(Cursor):
    def mover(self):
        print("Cursor do macOS movido")

class MacOSSelect(Select):
    def selecionar_opcao(self):
        print("Opção selecionada no macOS")

class MacOSInput(Input):
    def manipular_entrada(self):
        print("Entrada manipulada no macOS")

# Cliente
def cliente(fabrica: UIFactory):
    botao = fabrica.criar_botao()
    janela = fabrica.criar_janela()
    cursor = fabrica.criar_cursor()
    select = fabrica.criar_select()
    entrada = fabrica.criar_input()

    botao.clicar()
    janela.renderizar()
    cursor.mover()
    select.selecionar_opcao()
    entrada.manipular_entrada()

# Uso no cliente
if __name__ == "__main__":
    print("Cliente: Usando a interface do usuário do Windows")
    cliente(WindowsUIFactory())

    print("\nCliente: Usando a interface do usuário do macOS")
    cliente(MacOSUIFactory())
