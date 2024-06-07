import flet as ft
import sqlite3


def main(page: ft.Page):
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False
    page.title = 'itProger App'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def register(e):
        db = sqlite3.connect('it.proger')

        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            login TEXT,
            password TEXT
        )""")
        cur.execute(f"INSERT INTO users VALUES(NULL, '{user_login.value}', '{user_password.value}')")
        db.commit()
        db.close()

        user_login.value = ''
        user_password.value = ''
        btn_reg.text = 'Добавлено'
        page.update()

    def validate(e):
        if all([user_login.value, user_password.value]):
            btn_reg.disabled = False
            btn_auth.disabled = False
        else:
            btn_reg.disabled = True
            btn_auth.disabled = True
        page.update()

    def auth_user(e):
        db = sqlite3.connect('it.proger')

        cur = db.cursor()
        cur.execute(f"SELECT * FROM users WHERE login =  '{user_login.value}' AND password =  '{user_password.value}'")
        if cur.fetchone() != None:
            user_login.value = ''
            user_password.value = ''
            btn_auth.text = 'Авторизовано'
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text('Неверно введен логин или пароль'))
            page.snack_bar.open = True
            page.update()

        db.commit()
        db.close()

    user_login = ft.TextField(label='логин', width=200, on_change=validate)
    user_password = ft.TextField(label='пароль', password=True, width=200, on_change=validate)
    btn_reg = ft.ElevatedButton(text='Добавить', width=200, on_click=register, disabled=True)
    btn_auth = ft.ElevatedButton(text='Авторизовать', width=200, on_click=auth_user, disabled=True)

    panel_register = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Регистрация'),
                    user_login,
                    user_password,
                    btn_reg
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    panel_auth = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Авторизация'),
                    user_login,
                    user_password,
                    btn_auth
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()

        if index == 0:
            page.add(panel_register)
        elif index == 1:
            page.add(panel_auth)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER, label='Регистрация'),
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label='Авторизация')
        ], on_change=navigate
    )

    page.add(panel_register)


ft.app(target=main)
