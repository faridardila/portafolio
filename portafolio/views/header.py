import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data
from portafolio.styles.styles import Size


def header(data: Data) -> rx.Component:
    return rx.flex(
        rx.box(
            rx.avatar(
                src=data.avatar,
                size="8",
                radius="full",
                border="3px solid #0d0d17"
            ),
            class_name="avatar-container"
        ),
        rx.vstack(
            heading(data.name, True),
            rx.text(
                data.skill if data.skill else "Ingeniero de Sistemas",
                font_weight="600",
                color="#a855f7",
                font_size="1.2em",
                margin_top="-0.5em"
            ),
            rx.text(
                rx.icon("map-pin", size=18),
                data.location,
                display="flex",
                align_items="center",
                gap="4px",
                color="var(--gray-11)"
            ),
            media(data.media),
            spacing=Size.SMALL.value,
            align_items=["center", "flex-start"]
        ),
        spacing=Size.MEDIUM.value,
        flex_direction=["column", "row"],
        align_items="center",
        width="100%",
        text_align=["center", "left"]
    )
