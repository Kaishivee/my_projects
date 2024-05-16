import flet as ft
import requests


def main(page: ft.Page):
    page.window_width = 700
    page.window_height = 600
    page.window_resizable = False
    page.update()
    page.title = 'Погодная программа'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Введите город', width=400)
    wather_data = ft.Text('')

    def get_info(e):
        if len(user_data.value) < 2:
            return

        API = '1ac89e39f5ff865077fe27399e3fcb9f'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
        res = requests.get(URL).json()
        temp = res['main']['temp']
        wather_data.value = 'Погода ' + str(round(temp)) + '°С'
        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text('Погодная программа'),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([wather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text='Получить', on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
