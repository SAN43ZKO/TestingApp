from flet import *


class AppHeader(UserControl):
    def __init__(self):
        super().__init__()

    def app_header_logo(self):
        return Container(
            content=Text("Test App", size=15, color="#ffffff", weight=FontWeight.BOLD)
        )
    
    def app_header_search_bar(self):
        return Container(
            width=300,
            padding=8,
            bgcolor="white10",
            border_radius=10,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name=icons.SEARCH_ROUNDED, size=19, opacity=1, color="white"),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_color="white",
                        cursor_width=1,
                        hint_text="Search",
                        hint_style=TextStyle(
                            color="#ffffff"
                        ),
                        color="#ffffff",
                    )
                ]
            )
        )
    
    
    def app_header_acc(self):
        return Container(content=IconButton(icon=icons.PERSON))

    def build(self):
        return Container(
            padding=10,
            expand=True,
            height=60,
            bgcolor= "#081d33",
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                expand=True,
                controls=[
                    self.app_header_logo(),
                    self.app_header_search_bar(),
                    self.app_header_acc()
                ]
            )
        )