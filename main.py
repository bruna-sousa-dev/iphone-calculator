import flet as ft
from decimal import Decimal

class App:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.bgcolor = ft.colors.BLACK
        self.page.window_resizable = False
        self.page.window_width = 250
        self.page.window_height = 380
        self.page.title = 'Iphone Calculator'
        self.page.window_always_on_top = False
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.botoes = [
            {'operador': 'AC', 'fonte': ft.colors.BLACK, 'fundo': ft.colors.BLUE_GREY_100},
            {'operador': '±', 'fonte': ft.colors.BLACK, 'fundo': ft.colors.BLUE_GREY_100},
            {'operador': '%', 'fonte': ft.colors.BLACK, 'fundo': ft.colors.BLUE_GREY_100},
            {'operador': '/', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
            {'operador': '7', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
            {'operador': '8', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
            {'operador': '9', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
            {'operador': '*', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
            {'operador': '4', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
            {'operador': '5', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
            {'operador': '6', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
            {'operador': '-', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
            {'operador': '1', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
            {'operador': '2', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
            {'operador': '3', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
            {'operador': '+', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
            {'operador': '0', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
            {'operador': '.', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
            {'operador': '=', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
        ]
        self.main()

    def main(self):

        def calculate(operador, value_at):
            try:
                value = eval(value_at)
                if operador == '%':
                    value /= 100
                elif operador == '±':
                    value = -value
            except:
                return 'Error'
            
            digits = min(abs(Decimal(value).as_tuple().exponent), 6)
            return format(value, f'.{digits}f')

        def select(e):
            value_at = result.value if result.value not in ('0', 'Error') else ''
            value = e.control.content.value

            if value.isdigit():
                value = value_at + value
            elif value == 'AC':
                value = '0'
            else:
                if value_at and value_at[-1] in ('/', '*', '-', '+', '.'):
                    value_at = value_at[:-1]
                value = value_at + value
                if value[-1] in ('=', '%', '±'):
                    value = calculate(operador=value[-1], value_at=value_at)

            result.value = value
            result.update()

        result = ft.Text(value = '0', color = ft.colors.WHITE, size = 20)

        display = ft.Row(
            width = 250,
            controls = [result],
            alignment = ft.MainAxisAlignment.END
        )

        btn = [ft. Container(
            content = ft.Text(value = btn['operador'], color = btn['fonte']),
            width = 45,
            height = 45,
            bgcolor = btn['fundo'],
            border_radius = ft.border_radius.all(100),   
            alignment = ft.alignment.center, 
            on_click = select    
        ) for btn in self.botoes]

        keyboard = ft.Row(
            width = 250,
            wrap = True,
            controls = btn,
            alignment = ft.MainAxisAlignment.END,
        )

        layout = ft.Container(
            content = ft.Column(
                controls = [
                    display,
                    keyboard
                ]
            ),
            bgcolor = ft.colors.BLACK,
            padding = ft.padding.all(10),
            border_radius = 10,
            shadow = ft.BoxShadow(blur_radius = 50, color = ft.colors.WHITE)
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target = App, assets_dir = 'assets')
