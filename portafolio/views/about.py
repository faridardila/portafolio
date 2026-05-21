import reflex as rx
from portafolio.components.heading import heading
from portafolio.styles.styles import Size


def about(description: str) -> rx.Component:
    return rx.vstack(
        heading("Sobre mí"),
        rx.text(
            description,
            font_size="1.1em",
            line_height="1.75",
            color="var(--gray-11)",
            font_weight="400"
        ),
        spacing=Size.SMALL.value,
        width="100%"
    )
