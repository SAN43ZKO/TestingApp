from flet import *

def btn_add(page: Page):

    def close_dlg(self):
        modal_dlg.open = False
        page.update()


    modal_dlg = AlertDialog(
        modal=True,
        title=Text("Add new record", weight="bold"),
        content=Column(
            expand=True,
            width=500,
            height=250,
            controls=[
                TextField(label="First Name"),
                TextField(label="Last Name"),
                TextField(label="Age"),
            ]
        ),
        actions=[
            TextButton("Ok", height=50, on_click=close_dlg),
            TextButton("Cancel", height=50, on_click=close_dlg)
        ],
        actions_alignment=MainAxisAlignment.END
    )

    def open_dlg(self):
        page.dialog = modal_dlg
        modal_dlg.open = True
        page.update()
        

    return Container(
        padding=padding.only(right=10),
        alignment=alignment.center_right,
        content=ElevatedButton(
            on_click=open_dlg,
            bgcolor="#081d33",
            color="white",
            content=Row(
                controls=[
                    Icon(name=icons.ADD_ROUNDED, size=14),
                    Text("Add new record", size=14, weight="bold")
                    ]
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6)
                },
                color={
                    "": "white"
                }
            ),
            height=42,
            width=180
        )
    )

     