import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title, font_size="1.2em", color="#ffffff"),
                rx.text(info.subtitle, font_size="0.95em", color="#a855f7", font_weight="500"),
                rx.cond(
                    info.description != "",
                    rx.text(
                        info.description,
                        font_size="0.9em",
                        color="var(--gray-11)",
                        line_height="1.5",
                        white_space="pre-line"
                    )
                ),
                rx.cond(
                    len(info.technologies) > 0,
                    rx.flex(
                        *[
                            rx.badge(
                                rx.box(class_name=technology.icon),
                                technology.name,
                                class_name="tech-badge",
                                variant="soft"
                            )
                            for technology in info.technologies
                        ],
                        wrap="wrap",
                        spacing=Size.SMALL.value,
                        padding_top="0.3em"
                    )
                ),
                rx.hstack(
                    rx.cond(
                        info.url != "",
                        icon_button(
                            "link",
                            info.url
                        )
                    ),
                    rx.cond(
                        info.github != "",
                        icon_button(
                            "github",
                            info.github
                        )
                    ),
                    spacing=Size.SMALL.value,
                    padding_top="0.3em"
                ),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        rx.vstack(
            rx.cond(
                info.date != "",
                rx.badge(info.date, color_scheme="purple", variant="surface")
            ),
            rx.cond(
                info.certificate != "",
                icon_button(
                    "shield-check",
                    info.certificate,
                    solid=True
                )
            ),
            *[
                rx.box(
                    rx.image(
                        src=img,
                        height="auto",
                        width="100%",
                        border_radius=EmSize.DEFAULT.value,
                        object_fit="cover",
                        box_shadow="0 8px 16px rgba(0,0,0,0.3)"
                    ),
                    width=["100%", "280px"],
                    flex_shrink="0",
                    padding_top="0.4em"
                )
                for img in info.images
            ],
            spacing=Size.SMALL.value,
            align="end",
            flex_shrink="0",
            width=["100%", "auto"]
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        class_name="glass-card",
        width="100%",
        align_items="start"
    )
