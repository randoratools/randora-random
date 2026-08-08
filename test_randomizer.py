from __future__ import annotations

import pytest

from randomizer import select_winners


PARTICIPANTS = [
    {"participant_id": "participant-1"},
    {"participant_id": "participant-2"},
    {"participant_id": "participant-3"},
    {"participant_id": "participant-4"},
]


def test_selection_is_unique_and_has_requested_size() -> None:
    winners = select_winners(PARTICIPANTS, 3)

    assert len(winners) == 3
    assert len({winner["participant_id"] for winner in winners}) == 3


def test_duplicate_participants_are_rejected() -> None:
    with pytest.raises(ValueError, match="must be unique"):
        select_winners([PARTICIPANTS[0], PARTICIPANTS[0]], 1)


def test_impossible_count_is_rejected() -> None:
    with pytest.raises(ValueError, match="not enough participants"):
        select_winners(PARTICIPANTS, 5)


def test_non_positive_count_is_rejected() -> None:
    with pytest.raises(ValueError, match="must be positive"):
        select_winners(PARTICIPANTS, 0)
