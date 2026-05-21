import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.data import Info
from portafolio.styles.styles import Size


def info(title: str, info: list[Info]) -> rx.Component:
    if title == "Idiomas":
        return rx.vstack(
            heading(title),
            rx.flex(
                *[
                    rx.box(
                        info_detail(item),
                        width=["100%", "calc(50% - 8px)", "calc(33.3% - 12px)"],
                    )
                    for item in info
                ],
                wrap="wrap",
                spacing=Size.DEFAULT.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        )

    return rx.vstack(
        heading(title),
        rx.vstack(
            *[
                info_detail(item)
                for item in info
            ],
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
