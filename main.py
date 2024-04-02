import flet 
from flet import *
from header import AppHeader
from btn import btn_add

def main(page: Page):
    page.title = "testApp"
    page.spacing = 0
    page.padding = 0
    page.window_min_width = 650
    page.window_min_height = 700
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader(),
                btn_add(page)
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    flet.app(target=main)