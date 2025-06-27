from typing import List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def list_dictionary() -> None:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        ("EXECUTED", [41428829, 939719570]),
        ("CANCELED", [594226727, 615064591]),
    ],
)
def test_filter_by_state(list_dictionary: list, state: str, expected: list) -> None:
    filtered_data = filter_by_state(list_dictionary, state)
    assert [i["id"] for i in filtered_data] == expected


@pytest.mark.parametrize(
    "descending, expected",
    [
        (True, [41428829, 615064591, 594226727, 939719570]),
        (False, [939719570, 594226727, 615064591, 41428829]),
    ],
)
def test_sort_by_date(list_dictionary: list, descending: bool, expected: list) -> None:
    filtered_data = sort_by_date(list_dictionary, descending)
    assert [i["id"] for i in filtered_data] == expected
