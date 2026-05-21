import reflex as rx

from portafolio.styles.styles import EmSize


def icon_badge(icon: str) -> rx.Component:
    return rx.badge(
        rx.icon(
            icon,
            size=28
        ),
        aspect_ratio="1",
        variant="soft",
        color_scheme="purple",
        padding="0.5em",
        border_radius="12px"
    )
