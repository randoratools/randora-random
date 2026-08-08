from __future__ import annotations

import argparse
import json
import secrets
from pathlib import Path
from typing import Any


def select_winners(
    participants: list[dict[str, Any]],
    count: int,
) -> list[dict[str, Any]]:
    if count < 1:
        raise ValueError("count must be positive")
    if count > len(participants):
        raise ValueError("not enough participants")

    participant_ids = [participant["participant_id"] for participant in participants]
    if len(set(participant_ids)) != len(participant_ids):
        raise ValueError("participant_id values must be unique")

    random_source = secrets.SystemRandom()
    return random_source.sample(participants, count)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("participants", type=Path)
    parser.add_argument("count", type=int)
    args = parser.parse_args()

    participants = json.loads(args.participants.read_text(encoding="utf-8"))
    winners = select_winners(participants, args.count)
    print(json.dumps(winners, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
