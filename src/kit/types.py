from typing import Any, Literal, TypedDict, NotRequired


class CategoryData(TypedDict):
    yaml_option: NotRequired[list[str]]
    hidden: NotRequired[bool]
    _comment: NotRequired[str | list[str]]


type CategoryTableData = dict[str, CategoryData]


class StartingItemsData(TypedDict):
    items: NotRequired[list[str]]
    item_categories: NotRequired[list[str]]
    random: NotRequired[int]
    if_previous_item: NotRequired[list[str]]
    yaml_option: NotRequired[list[str]]
    _comment: NotRequired[str | list[str]]


class GameData(TypedDict):
    game: str
    player: NotRequired[str]
    creator: NotRequired[str]
    filler_item_name: str
    starting_items: NotRequired[list[StartingItemsData]]
    death_link: NotRequired[bool]
    starting_index: NotRequired[int]
    _comment: NotRequired[str | list[str]]


class GameTableData(TypedDict):
    schema: NotRequired[str]
    game: str
    player: NotRequired[str]
    creator: NotRequired[str]
    filler_item_name: str
    starting_items: NotRequired[list[StartingItemsData]]
    death_link: NotRequired[bool]
    starting_index: NotRequired[int]
    _comment: NotRequired[str | list[str]]


class ItemData(TypedDict):
    name: str
    category: NotRequired[str | list[str]]
    count: NotRequired[str | int]
    value: NotRequired[dict[str, int]]
    progression: NotRequired[bool]
    progression_skip_balancing: NotRequired[bool]
    useful: NotRequired[bool]
    trap: NotRequired[bool]
    filler: NotRequired[bool]
    early: NotRequired[bool | int]
    local: NotRequired[bool]
    local_early: NotRequired[bool | int]
    id: NotRequired[int]
    _comment: NotRequired[str | list[str]]


class ItemTableData(TypedDict):
    schema: NotRequired[str]
    data: NotRequired[list[ItemData]]
    _comment: NotRequired[str | list[str]]


class RequireData(TypedDict):
    or_: NotRequired[list[str]]


class LocationData(TypedDict):
    name: str
    category: NotRequired[str | list[str]]
    requires: NotRequired[str | list[str | RequireData]]
    region: NotRequired[str]
    place_item: NotRequired[list[str]]
    dont_place_item: NotRequired[list[str]]
    place_item_category: NotRequired[list[str]]
    dont_place_item_category: NotRequired[list[str]]
    victory: NotRequired[bool]
    prehint: NotRequired[bool]
    hint_entrance: NotRequired[str]
    id: NotRequired[int]
    _comment: NotRequired[str | list[str]]


class LocationTableData(TypedDict):
    schema: NotRequired[str]
    data: NotRequired[list[LocationData]]
    _comment: NotRequired[str | list[str]]


class RegionData(TypedDict):
    requires: NotRequired[str | list[str | RequireData]]
    connects_to: NotRequired[list[str]]
    starting: NotRequired[bool]
    exit_requires: NotRequired[dict[str, str | list[str | RequireData]]]
    entrance_requires: NotRequired[dict[str, str | list[str | RequireData]]]
    _comment: NotRequired[str | list[str]]


class RegionTableData(TypedDict):
    schema: NotRequired[str]


class TutorialData(TypedDict):
    name: str
    description: str
    language: str
    file_name: str
    link: NotRequired[str]
    authors: NotRequired[list[str]]
    _comment: NotRequired[str | list[str]]


class WebData(TypedDict):
    options_page: NotRequired[bool | str]
    game_info_languages: NotRequired[list[str]]
    theme: NotRequired[str]
    bug_report_page: NotRequired[str]
    tutorials: NotRequired[list[TutorialData]]
    options_presets: NotRequired[dict[str, dict[str, Any]]]
    _comment: NotRequired[str | list[str]]


class DocsData(TypedDict):
    apworld_description: NotRequired[list[str]]
    web: NotRequired[WebData]
    _comment: NotRequired[str | list[str]]


class MetaData(TypedDict):
    docs: NotRequired[DocsData]
    enable_region_diagram: NotRequired[bool]
    _comment: NotRequired[str | list[str]]


class MetaTableData(TypedDict):
    schema: NotRequired[str]
    docs: NotRequired[DocsData]
    enable_region_diagram: NotRequired[bool]
    _comment: NotRequired[str | list[str]]


class OptionBaseData(TypedDict):
    display_name: NotRequired[str]
    description: NotRequired[str | list[str]]
    rich_text_doc: NotRequired[bool]
    group: NotRequired[str]
    hidden: NotRequired[bool]
    visibility: NotRequired[str | list[str] | int]
    _comment: NotRequired[str | list[str]]


class ToggleOptionData(OptionBaseData):
    type: Literal["Toggle"]
    default: bool


class ChoiceOptionData(OptionBaseData):
    type: Literal["Choice"]
    values: dict[str, int]
    aliases: NotRequired[dict[str, int | str]]
    default: NotRequired[int]
    allow_custom_value: NotRequired[bool]


class RangeOptionData(OptionBaseData):
    type: Literal["Range"]
    range_start: NotRequired[int]
    range_end: NotRequired[int]
    default: NotRequired[int]
    values: NotRequired[dict[str, int]]


class CoreOptionData(OptionBaseData):
    default: NotRequired[int | bool]
    aliases: NotRequired[dict[str, int | str]]
    values: NotRequired[dict[str, int]]


type OptionData = ToggleOptionData | ChoiceOptionData | RangeOptionData | CoreOptionData


class OptionsData(TypedDict):
    core: NotRequired[dict[str, CoreOptionData]]
    user: NotRequired[dict[str, OptionData]]
    _comment: NotRequired[str | list[str]]


class OptionsTableData(TypedDict):
    schema: NotRequired[str]
    core: NotRequired[dict[str, CoreOptionData]]
    user: NotRequired[dict[str, OptionData]]
    _comment: NotRequired[str | list[str]]


type RegionTableData = dict[str, RegionData]
