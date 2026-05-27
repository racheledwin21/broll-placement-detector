VISUAL_WORDS = [
    "forest",
    "valley",
    "river",
    "coffee",
    "beans",
    "deck",
    "shops",
    "mug",
    "roastery",
    "town"
]

NEGATIVE_WORDS = [
    "subscribe",
    "welcome",
    "thanks",
    "see you next time"
]

def detect_broll_segments(segments):

    results = []

    for seg in segments:

        text = seg["text"].lower()

        if any(word in text for word in NEGATIVE_WORDS):
            continue

        score = 0

        for word in VISUAL_WORDS:
            if word in text:
                score += 2

        if score >= 2:
            results.append({
                "start": seg["start"],
                "end": seg["end"],
                "reason": "Contains strong visual elements"
            })

    return results