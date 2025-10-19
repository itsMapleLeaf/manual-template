from typing import Any, Literal, TypedDict, NotRequired


class MetaData(TypedDict):
    docs: NotRequired["DocsData"]
    enable_region_diagram: NotRequired[bool]


class DocsData(TypedDict):
    apworld_description: NotRequired[list[str]]
    web: NotRequired["WebData"]


class WebData(TypedDict):
    options_page: NotRequired[bool | str]
    game_info_languages: NotRequired[list[str]]
    theme: NotRequired[str]
    bug_report_page: NotRequired[str]
    tutorials: NotRequired[list["TutorialData"]]
    options_presets: NotRequired[dict[str, dict[str, Any]]]


class TutorialData(TypedDict):
    name: str
    description: str
    language: str
    file_name: str
    link: NotRequired[str]
    authors: NotRequired[list[str]]
