movies = {
    "Interstellar": ["sci-fi", "space", "adventure"],
    "The Matrix": ["sci-fi", "action", "technology"],
    "Inception": ["sci-fi", "thriller", "action"],
    "John Wick": ["action", "thriller"],
    "The Dark Knight": ["action", "crime"],
    "Titanic": ["romance", "drama"],
    "La La Land": ["romance", "music"],
    "The Notebook": ["romance", "drama"],
    "The Conjuring": ["horror", "thriller"],
    "Insidious": ["horror", "supernatural"],
    "Jumanji": ["comedy", "adventure"],
    "Free Guy": ["comedy", "action", "gaming"]
}

print("=" * 60)
print("🎬 AI Recommendation Engine")
print("=" * 60)

name = input("Enter your name: ")

print("\nAvailable Interests:")
print("action, sci-fi, romance, comedy, horror")
print("thriller, adventure, drama, space, gaming")
print("crime, technology, supernatural, music")

user_input = input(
    "\nEnter interests separated by commas: "
).lower()

user_preferences = [
    interest.strip()
    for interest in user_input.split(",")
]

scores = {}

for movie, tags in movies.items():
    score = 0

    for preference in user_preferences:
        if preference in tags:
            score += 1

    scores[movie] = score

recommended = sorted(
    scores.items(),
    key=lambda x: x[1],
    reverse=True
)

print(f"\n📌 Top Recommendations for {name}\n")

count = 0

for movie, score in recommended:
    if score > 0:
        print(f"⭐ {movie}  | Match Score: {score}")
        count += 1

    if count == 5:
        break

if count == 0:
    print("No matching recommendations found.")