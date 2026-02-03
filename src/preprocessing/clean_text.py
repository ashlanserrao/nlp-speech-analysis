import re

STAGE_DIRECTIONS = {
    r"\[laughter\]": "<LAUGHTER>",
    r"\[applause\]": "<APPLAUSE>",
    r"\[cheers\]": "<CHEERS>",
    r"\[music\]": "<MUSIC>",
    r"\[audience.*?\]": "<AUDIENCE>",
    r"\[.*?music.*?\]": "<MUSIC>",
    r"\[.*?applause.*?\]": "<APPLAUSE>",
    r"\[.*?laughter.*?\]": "<LAUGHTER>",
    r"\[announcer\]": "<SPEAKER>",
    r"\[camera.*?\]": "<SFX>"
}

def normalize_whitespace(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def replace_stage_directions(text: str) -> str:
    for pattern, token in STAGE_DIRECTIONS.items():
        text = re.sub(pattern, token, text, flags=re.IGNORECASE)

    return text

def strip_leading_title(text: str) -> str:
    """
    Remove a likely title
    """
    lines = text.split("\n")
    if len(lines) == 0:
        return text
    
    first_line = lines[0]

    # Heuristic titles are short, capital heavy and contain year or colon

    if (
        len(first_line) < 150
        and (":" in first_line or "(" in first_line)
        and first_line.strip().istitle() or first_line.strip().isupper()
    ):
        return "\n".join(lines[1:]).strip()
    
    return text

def basic_clean(text: str) -> str:
    """
    Safe cleaning that preserves meaning.
    """
    text = strip_leading_title(text)
    text = normalize_whitespace(text)
    text = replace_stage_directions(text)
    return text

def lowercase(text: str) -> str:
    return text.lower()

