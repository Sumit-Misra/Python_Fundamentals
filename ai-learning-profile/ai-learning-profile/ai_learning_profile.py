# This script:
# - Asks the user for basic profile details
# - Asks for skills, study hours, and performance score
# - Processes strings, numbers, and formats output nicely
# - Demonstrates input(), print(), f-strings, string methods,
#   input processing, number functions, and type conversion.

print("=" * 50)
print("      AI LEARNING PROFILE GENERATOR")
print("=" * 50)
print()

# -------------------------------
# 1. Basic Personal Information
# -------------------------------

full_name = input("Enter your full name: ").strip()
age_str = input("Enter your age (in years): ").strip()
country = input("Enter your country: ").strip()
profession = input("Enter your current role/profession: ").strip()

age = int(age_str)  # type conversion (string -> int)

# Clean formatting for display

full_name_title = full_name.title()
country_title = country.title()
profession_title = profession.title()

print()
print("-" * 50)
print("BASIC PROFILE")
print("-" * 50)

print(f"Name      : {full_name_title}")
print(f"Age       : {age}")
print(f"Country   : {country_title}")
print(f"Profession: {profession_title}")
print()

# ----------------------------------------
# 2. Skills and Focus Areas (Strings + split)
# ----------------------------------------

skills_input = input(
    "Enter 3 key skills (comma-separated, e.g. Python,SQL,Git): "
).strip()

skill1, skill2, skill3 = skills_input.split(",")

skill1 = skill1.strip().title()
skill2 = skill2.strip().title()
skill3 = skill3.strip().title()

print()
print("-" * 50)
print("SKILL SET")
print("-" * 50)
print(f"Skill 1: {skill1}")
print(f"Skill 2: {skill2}")
print(f"Skill 3: {skill3}")
print()

# ----------------------------------------
# 3. Study Time & Learning Metrics
# ----------------------------------------

print("Enter your study hours for the LAST 3 days (space-separated, e.g. 1.5 2 0.5)")
study_input = input("Study hours (3 values): ").strip()

h1_str, h2_str, h3_str = study_input.split()

h1 = float(h1_str)
h2 = float(h2_str)
h3 = float(h3_str)

total_hours = h1 + h2 + h3
avg_hours = total_hours / 3
max_hours = max(h1, h2, h3)
min_hours = min(h1, h2, h3)

target_avg = 2.0  # target hours per day
difference_from_target = avg_hours - target_avg
difference_from_target_abs = abs(difference_from_target)

print()
print("-" * 50)
print("LEARNING HOURS SUMMARY")
print("-" * 50)

print(f"Day 1 hours: {h1:.2f}")
print(f"Day 2 hours: {h2:.2f}")
print(f"Day 3 hours: {h3:.2f}")
print()
print(f"Total hours (3 days): {total_hours:.2f}")
print(f"Average hours / day : {avg_hours:.2f}")
print(f"Max hours in a day  : {max_hours:.2f}")
print(f"Min hours in a day  : {min_hours:.2f}")
print()
print(f"Target average (hrs/day): {target_avg:.2f}")
print(f"Difference from target  : {difference_from_target:.2f}")
print(f"Abs difference (ignore sign): {difference_from_target_abs:.2f}")
print()

# ----------------------------------------
# 4. Simple Numeric Performance Metric
# ----------------------------------------

print("Now, enter your recent learning performance score.")
print("For example: percentage of tasks completed out of 100.")
score_str = input("Enter your performance score (0-100): ").strip()
score = float(score_str)

score_fraction = score / 100  # 0.0–1.0
rounded_score = round(score, 2)

print()
print("-" * 50)
print("PERFORMANCE SUMMARY")
print("-" * 50)

print(f"Raw score      : {score}")
print(f"Rounded score  : {rounded_score:.2f}")
print(f"As fraction    : {score_fraction:.4f}")
print(f"As percentage  : {score_fraction:.2%}")
print()

# ----------------------------------------
# 5. Short Motto / Quote Analysis (Strings)
# ----------------------------------------

motto = input("Enter a short learning motto or quote: ").strip()

motto_lower = motto.lower()
motto_len = len(motto)
count_a = motto_lower.count("a")

# Safely get first and last characters (if motto is not empty)
first_char = motto[0] if motto_len > 0 else ""
last_char = motto[-1] if motto_len > 0 else ""

print()
print("-" * 50)
print("MOTTO ANALYSIS")
print("-" * 50)

print(f"Original motto : {motto}")
print(f"Lowercase      : {motto_lower}")
print(f"Length         : {motto_len}")
print(f"Count of 'a'   : {count_a}")
print(f"First character: {first_char}")
print(f"Last character : {last_char}")
print()

# ----------------------------------------
# 6. Small Cleaned Summary Line (join / strip / bool)
# ----------------------------------------

notes = input("Enter any additional notes (or press Enter to skip): ")

notes_clean = notes.strip()
has_notes = bool(notes_clean)

words_summary = [
    full_name_title,
    "from",
    country_title,
    "is learning AI with focus on",
    skill1 + ",",
    skill2,
    "and",
    skill3 + ".",
]

summary_line = " ".join(words_summary)

print()
print("-" * 50)
print("FINAL SUMMARY")
print("-" * 50)
print(summary_line)
print()

print(f"Any additional notes provided? {has_notes}")
print("Notes (cleaned):", notes_clean)
print()

# ----------------------------------------
# 7. Pretty Final Report Block (Alignment & Formatting)
# ----------------------------------------

print("=" * 50)
print("            AI LEARNING REPORT")
print("=" * 50)

print(f"{'Name':<12}: {full_name_title}")
print(f"{'Age':<12}: {age}")
print(f"{'Country':<12}: {country_title}")
print(f"{'Profession':<12}: {profession_title}")
print()

print(f"{'Skill 1':<12}: {skill1}")
print(f"{'Skill 2':<12}: {skill2}")
print(f"{'Skill 3':<12}: {skill3}")
print()

print(f"{'Total Hours':<12}: {total_hours:6.2f}")
print(f"{'Avg Hours':<12}: {avg_hours:6.2f}")
print(f"{'Max Hours':<12}: {max_hours:6.2f}")
print(f"{'Min Hours':<12}: {min_hours:6.2f}")
print()

print(f"{'Score %':<12}: {score_fraction:6.2%}")
print(f"{'Raw Score':<12}: {score:6.2f}")
print()

print("Motto:")
print(f"\"{motto}\"")
print("=" * 50)
print("         END OF AI LEARNING PROFILE")
print("=" * 50)
