from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

VISUAL_KEYWORDS = [
    "cinematic",
    "sunset",
    "food",
    "reaction",
    "gameplay",
    "aesthetic",
    "crowd",
    "lights",
    "beautiful",
    "music",
    "coffee",
    "city",
    "rooftop",
    "neon",
    "camera",
    "shot",
    "view",
    "dramatic",
    "emotional",
    "exciting"
]


@app.post("/detect")
async def detect(data: dict):

    transcript = data.get("transcript", "").lower()

    words = transcript.split()

    placements = []

    used_keywords = set()

    for i, word in enumerate(words):

        cleaned_word = word.strip(".,!?")

        if cleaned_word in VISUAL_KEYWORDS and cleaned_word not in used_keywords:

            used_keywords.add(cleaned_word)

            start = round(i * 0.6, 1)
            end = round(start + 4.5, 1)

            placements.append({
                "start": f"{start}s",
                "end": f"{end}s",
                "reason": f"Detected visual keyword: {cleaned_word}",
                "confidence": "92%"
            })

    if not placements:
        placements.append({
            "start": "0.0s",
            "end": "5.0s",
            "reason": "General introductory visual detected",
            "confidence": "75%"
        })

    return {
        "placements": placements,
        "total_detected": len(placements),
        "status": "success"
    }