import flet as ft
from WebN.Config import get_env_key as WebN

top_headlines = []


def set_up_screen(data):
    global top_headlines
    top_headlines = data
    ft.app(target=main)


def main(page: ft.Page):
    page_title = ft.Text(WebN('APP_NAME'), size=30)

    # Start search box
    def close_anchor(e):
        text = f"{e.control.data}"
        print(f"closing view from {text}")
        rail.selected_index = 0
        anchor.close_view(text)
        page.update()

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(e):
        print(f"handle_tap")
        rail.selected_index = 3
        anchor.open_view()
        page.update()

    anchor = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.GREY_50,
        bar_hint_text="Искать новости",
        view_hint_text="Начните поиск . . .",
        width=page.window_max_width,
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=handle_tap,
        controls=[
            ft.ListTile(title=ft.Text(f'{i}'), on_click=close_anchor, data=i)
            for i in range(10)
        ],
    )
    # Start search box

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Предложить"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME_FILLED, label="Главная"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.SOURCE),
                selected_icon_content=ft.Icon(ft.icons.SOURCE_SHARP),
                label="Источники",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOK_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Избранное",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.SEARCH_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.SEARCH),
                label="Найти",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Настройки"),
            ),
        ],
        on_change=lambda e: page_title_as_nav_id(e.control.selected_index),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column(
                    [
                        page_title,
                        anchor,
                    ],
                    alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        ),

    )

    def set_page_title(pg_title=None):
        if pg_title == None:
            page_title.visible = False
            page_title.value = ''
            page.update()
        else:
            page_title.visible = True
            page_title.value = pg_title
            page.update()

    def page_title_as_nav_id(nav_id):
        print(nav_id)
        if nav_id == 0:
            set_page_title("Главная")
        elif nav_id == 1:
            set_page_title("Источники")
        elif nav_id == 2:
            set_page_title("Избранное")
        elif nav_id == 3:
            set_page_title('')
            anchor.open_view()
        elif nav_id == 4:
            set_page_title("Настройки")
        else:
            set_page_title(WebN('APP_NAME'))
