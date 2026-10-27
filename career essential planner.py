print("CAREER ESSENTIALS PLANNER")
print("-------------------------")

skills = [
    "Communication",
    "Teamwork",
    "Problem Solving",
    "Time Management",
    "Technical Skills"
]

ratings = {}

for skill in skills:
    while True:
        try:
            rating = int(input(f"Rate your {skill} (1-5): "))

            if 1 <= rating <= 5:
                ratings[skill] = rating
                break

            print("Enter a number between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")

print("\nCAREER SKILL REPORT")
print("-------------------")

for skill, rating in ratings.items():
    print(f"{skill}: {rating}/5")

average = sum(ratings.values()) / len(ratings)

print("\nAverage skill rating:", round(average, 2), "/5")

print("\nAREAS TO IMPROVE")

found = False

for skill, rating in ratings.items():
    if rating < 4:
        print("-", skill)
        found = True

if not found:
    print("Great! Keep developing your skills.")

print("\nCareer assessment completed!")