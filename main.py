import os

TEXT = "My last day is Friday, unless the printer jams again, in which case it was yesterday."


def main():
    assert 1 <= len(TEXT) <= 140 and TEXT.strip(), "gate: 1-140 chars, not whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
