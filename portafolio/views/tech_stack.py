import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Technology
from portafolio.styles.styles import EmSize, Size


def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        heading("Tecnologías"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=technology.icon,
                        font_size="18px"
                    ),
                    rx.text(technology.name, font_size="14px"),
                    size="2",
                    class_name="tech-badge",
                    variant="soft"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.DEFAULT.value
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
