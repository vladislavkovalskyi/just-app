import flet as ft


async def registration(page: ft.Page):
    page.title = "Just App | Registration"
    page.window.height = 700
    page.window.width = 400
    page.bgcolor = ft.colors.WHITE

    registration = ft.Column(
        controls=[
            ft.Image("gui-app/assets/logo.png", width=150, height=150),
            ft.Container(
                ft.TextField(
                    label="Login",
                    border_color=ft.colors.GREY_800,
                    focused_border_color=ft.colors.PINK_ACCENT,
                    color=ft.colors.GREY_800,
                    cursor_color=ft.colors.PINK_ACCENT,
                    label_style=ft.TextStyle(color=ft.colors.GREY_800),
                    max_length=20,
                    autofocus=True
                ),
                padding=ft.Padding(20, 0, 20, 0)
            ),
            ft.Container(
                ft.TextField(
                    label="E-mail",
                    border_color=ft.colors.GREY_800,
                    focused_border_color=ft.colors.PINK_ACCENT,
                    color=ft.colors.GREY_800,
                    cursor_color=ft.colors.PINK_ACCENT,
                    label_style=ft.TextStyle(color=ft.colors.GREY_800),
                    autofocus=True
                ),
                padding=ft.Padding(20, 0, 20, 20)
            ),
            ft.Container(
                ft.TextField(
                    label="Password",
                    password=True,
                    border_color=ft.colors.GREY_800,
                    focused_border_color=ft.colors.PINK_ACCENT,
                    color=ft.colors.GREY_800,
                    cursor_color=ft.colors.PINK_ACCENT,
                    label_style=ft.TextStyle(color=ft.colors.GREY_800),
                ),
                padding=ft.Padding(20, 0, 20, 20)
            ),
            ft.Container(
                ft.TextField(
                    label="Retype password",
                    password=True,
                    border_color=ft.colors.GREY_800,
                    focused_border_color=ft.colors.PINK_ACCENT,
                    color=ft.colors.GREY_800,
                    cursor_color=ft.colors.PINK_ACCENT,
                    label_style=ft.TextStyle(color=ft.colors.GREY_800),
                ),
                padding=ft.Padding(20, 0, 20, 20)
            ),
            ft.Row(
                controls=[
                    ft.FilledButton(
                        "Sign up",
                        width=160,
                        height=50,
                        style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.PINK_ACCENT),
                        icon=ft.icons.APP_REGISTRATION,
                        on_click=lambda e: print("Sign up clicked")  # Обработка регистрации
                    ),
                    ft.FilledButton(
                        "Sign in",
                        width=160,
                        height=50,
                        style=ft.ButtonStyle(color=ft.colors.GREY_800, bgcolor=ft.colors.GREY_200),
                        icon=ft.icons.LOGIN,
                        on_click=lambda e: show_auth(page)  # Переход на авторизацию
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            ft.Container(
                ft.Text("by Vladyslav Kovalskyi", color=ft.colors.GREY_500),
                padding=ft.Padding(0, 20, 0, 0),  # Отступ сверху
                alignment=ft.alignment.center,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(
        registration
    )

async def main(page: ft.Page):
    page.title = "Just App | Auth"
    page.window.height = 700
    page.window.width = 400
    page.bgcolor = ft.colors.WHITE

    auth = ft.Column(
        controls=[
            ft.Image("gui-app/assets/logo.png", width=150, height=150),
            ft.Container(
                ft.TextField(
                    label="Login",
                    border_color=ft.colors.GREY_800,
                    focused_border_color=ft.colors.PINK_ACCENT,
                    color=ft.colors.GREY_800,
                    cursor_color=ft.colors.PINK_ACCENT,
                    label_style=ft.TextStyle(color=ft.colors.GREY_800),
                    max_length=20,
                    autofocus=True
                ),
                padding=ft.Padding(20, 0, 20, 0)
            ),
            ft.Container(
                ft.TextField(
                    label="Password",
                    password=True,
                    border_color=ft.colors.GREY_800,
                    focused_border_color=ft.colors.PINK_ACCENT,
                    color=ft.colors.GREY_800,
                    cursor_color=ft.colors.PINK_ACCENT,
                    label_style=ft.TextStyle(color=ft.colors.GREY_800),
                ),
                padding=ft.Padding(20, 0, 20, 20)
            ),
            ft.Row(
                controls=[
                    ft.FilledButton(
                        "Sign in",
                        width=160,
                        height=50,
                        style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.PINK_ACCENT),
                        icon=ft.icons.LOGIN,
                        on_click=lambda e: print("Sign in clicked")
                    ),
                    ft.FilledButton(
                        "Sign up",
                        width=160,
                        height=50,
                        style=ft.ButtonStyle(color=ft.colors.GREY_800, bgcolor=ft.colors.GREY_200),
                        icon=ft.icons.APP_REGISTRATION,
                        on_click=lambda e: print("Sign up clicked")
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            ft.Container(
                ft.Text("by Vladyslav Kovalskyi", color=ft.colors.GREY_500),
                padding=ft.Padding(0, 20, 0, 0),
                alignment=ft.alignment.center,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(
        auth
    )

ft.app(target=main)
