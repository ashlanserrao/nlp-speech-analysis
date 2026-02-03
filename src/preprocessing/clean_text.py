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

def basic_clean(text: str) -> str:
    """
    Safe cleaning that preserves meaning.
    """
    text = normalize_whitespace(text)
    text = replace_stage_directions(text)
    return text

def lowercase(text: str) -> str:
    return text.lower()

