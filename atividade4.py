'''
Considere que você está desenvolvendo um framework de renderização de gráficos que deve suportar diferentes bibliotecas gráficas (por exemplo, OpenGL, DirectX). 
Use o padrão Abstract Factory para definir uma interface comum para criar famílias de objetos relacionados à renderização (como renderizadores de texturas, sombras e modelos).
Em seguida, implemente cada fábrica concreta como um Singleton para garantir que apenas uma instância de cada fábrica seja usada durante a execução do programa. Demonstre como
um cliente pode usar esses padrões combinados para acessar recursos de renderização.
'''

# Interface para a fábrica abstrata
class GraphicsFactory:
    def create_texture_renderer(self):
        pass

    def create_shadow_renderer(self):
        pass

    def create_model_renderer(self):
        pass


# Fábrica concreta para OpenGL
class OpenGLGraphicsFactory(GraphicsFactory):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_texture_renderer(self):
        return OpenGLTextureRenderer()

    def create_shadow_renderer(self):
        return OpenGLShadowRenderer()

    def create_model_renderer(self):
        return OpenGLModelRenderer()


# Fábrica concreta para DirectX
class DirectXGraphicsFactory(GraphicsFactory):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_texture_renderer(self):
        return DirectXTextureRenderer()

    def create_shadow_renderer(self):
        return DirectXShadowRenderer()

    def create_model_renderer(self):
        return DirectXModelRenderer()


# Classes de renderização para OpenGL
class OpenGLTextureRenderer:
    def render(self):
        print("Rendering texture using OpenGL")


class OpenGLShadowRenderer:
    def render(self):
        print("Rendering shadows using OpenGL")


class OpenGLModelRenderer:
    def render(self):
        print("Rendering model using OpenGL")


# Classes de renderização para DirectX
class DirectXTextureRenderer:
    def render(self):
        print("Rendering texture using DirectX")


class DirectXShadowRenderer:
    def render(self):
        print("Rendering shadows using DirectX")


class DirectXModelRenderer:
    def render(self):
        print("Rendering model using DirectX")


# Cliente
def main():
    # Usando OpenGL
    opengl_factory = OpenGLGraphicsFactory()
    opengl_texture_renderer = opengl_factory.create_texture_renderer()
    opengl_shadow_renderer = opengl_factory.create_shadow_renderer()
    opengl_model_renderer = opengl_factory.create_model_renderer()

    # Usando DirectX
    directx_factory = DirectXGraphicsFactory()
    directx_texture_renderer = directx_factory.create_texture_renderer()
    directx_shadow_renderer = directx_factory.create_shadow_renderer()
    directx_model_renderer = directx_factory.create_model_renderer()

    # O cliente pode agora utilizar os renderizadores específicos conforme necessário
    opengl_texture_renderer.render()
    opengl_shadow_renderer.render()
    opengl_model_renderer.render()

    directx_texture_renderer.render()
    directx_shadow_renderer.render()
    directx_model_renderer.render()


if __name__ == "__main__":
    main()
