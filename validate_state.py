#!/usr/bin/env python3
"""Validate .agent/state.json with lightweight checks.

This script intentionally avoids external dependencies so it can run in most
Python environments.
"""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".agent" / "state.json"

REQUIRED = [
    "task_id",
    "task_name",
    "status",
    "current_role",
    "current_step",
    "goal",
    "todo",
    "done",
    "next_action",
    "updated_at",
]

VALID_STATUS = {
    "planning",
    "designing",
    "executing",
    "testing",
    "review_required",
    "documenting",
    "blocked",
    "done",
}

VALID_ROLES = {
    "Planner",
    "Architect",
    "Executor",
    "Tester",
    "Reviewer",
    "Documenter",
}


def main() -> int:
    if not STATE.exists():
        print(f"ERROR: {STATE} が存在しません。")
        return 1

    with STATE.open(encoding="utf-8") as f:
        data = json.load(f)

    errors = []
    for key in REQUIRED:
        if key not in data:
            errors.append(f"必須キーがありません: {key}")

    if data.get("status") not in VALID_STATUS:
        errors.append(f"status が不正です: {data.get('status')}")

    if data.get("current_role") not in VALID_ROLES:
        errors.append(f"current_role が不正です: {data.get('current_role')}")

    for key in ["todo", "done"]:
        if key in data and not isinstance(data[key], list):
            errors.append(f"{key} は配列である必要があります。")

    if errors:
        print("state.json の検証に失敗しました。")
        for error in errors:
            print(f"- {error}")
        return 1

    print("state.json は有効です。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
