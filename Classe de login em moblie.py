from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="Usuário:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="Senha:"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MeuAplicativo(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    MeuAplicativo().run()
    
Neste exemplo, estamos criando uma classe LoginScreen que herda de BoxLayout e cria uma tela de login com dois campos de texto para usuário e senha.
Em seguida, estamos criando uma classe MeuAplicativo que herda de App e retorna a tela de login como a raiz da interface do usuário. Finalmente, 
estamos executando o aplicativo.

Para rodar o aplicativo em um dispositivo móvel, você precisará compilá-lo para a plataforma específica usando um ferramenta de compilação, como o Buildozer.
 Além disso, você pode querer considerar adicionar recursos adicionais ao seu aplicativo, como botões, gráficos, animações, etc.
 A documentação do Kivy fornece muitas informações sobre como adicionar esses recursos.




