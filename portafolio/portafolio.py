import reflex as rx
from portafolio import data
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.extra import extra
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack

DATA = data.data


def index() -> rx.Component:
    return rx.box(
        # Background animated glowing blobs
        rx.box(class_name="bg-blob blob-1"),
        rx.box(class_name="bg-blob blob-2"),
        rx.box(class_name="bg-blob blob-3"),
        
        # Main center container
        rx.center(
            rx.vstack(
                header(DATA),
                about(DATA.about),
                rx.divider(opacity="0.15"),
                tech_stack(DATA.technologies),
                info("Proyectos", DATA.projects),
                info("Logros", DATA.achievements),
                info("Formación", DATA.training),
                info("Idiomas", DATA.experience),
                #extra(DATA.extras),
                rx.divider(opacity="0.15"),
                footer(DATA.media),
                class_name="glass-wrapper",
                spacing=Size.MEDIUM.value,
                max_width=MAX_WIDTH,
                width="100%"
            ),
            padding_x=["0.5em", "1em", "2em"],
            padding_y=["2em", "3em", "4em"],
            width="100%"
        ),
        width="100%",
        min_height="100vh",
        position="relative"
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        accentColor="purple", 
        grayColor="slate", 
        radius="full",
        scaling="105%",
        appearance="dark"
    )
)

title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image}
    ]
)
