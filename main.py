"""The Funniest Office Joke, Judged Head to Head.

Writes one short joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt: the out-of-office reply that quotes
"per my last email", so even the writer's absence turns out to be
passive-aggressive. Standard library only.
"""

import os

JOKE = (
    "I put 'per my last email' in my out-of-office reply. "
    "Even my absence is passive-aggressive now."
)


def joke_ok(text):
    """Check the joke against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: one joke about office life, a real joke
    with a setup and a turn and the punchline last. Returns the
    cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("joke must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "joke is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("joke must be exactly one line")
    return cleaned


def joke_report(text):
    """Measure the joke for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A one-liner too short to carry a setup and a turn
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = joke_ok(JOKE)
    report = joke_report(text)
    if report["words"] < 5:
        raise ValueError("joke is too short to carry a setup and a turn")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
