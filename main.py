"""One Line, One Laugh (plucky-finch-20) — a make.fun entry.

Prints exactly one funny line of text, at most 200 characters.
"""

LINE = (
    "All my houseplants are fake now. There is only so much rejection "
    "from living things."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
