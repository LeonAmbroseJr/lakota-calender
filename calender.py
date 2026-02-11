from datetime import datetime, timedelta

# List of Sacred Moons
lakota_moons = [
    {"lakota": "Wiótheȟika Wi", "english": "Moon of Hard Times"},
    {"lakota": "Čhaŋnápopa Wi", "english": "Trees Crack Moon"},
    {"lakota": "Ištáwičhayazan Wi", "english": "Sore Eyes Moon"},
    {"lakota": "Maǧá Okáda Wi", "english": "Geese Lay Eggs Moon"},
    {"lakota": "Wóžupi Wi", "english": "Planting Moon"},
    {"lakota": "Wípazuka Wasté Wi", "english": "Good Berries Moon"},
    {"lakota": "Čhaŋpȟásapa Wi", "english": "Ripe Chokecherries Moon"},
    {"lakota": "Wasútȟuŋ Wi", "english": "Harvest Moon"},
    {"lakota": "Čhaŋwápeǧi Wi", "english": "Brown Leaves Moon"},
    {"lakota": "Čhaŋwápekasna Wi", "english": "Falling Leaves Moon"},
    {"lakota": "Waníyetu Wi", "english": "Winter Moon"},
    {"lakota": "Waníčhokaŋ Wi", "english": "Midwinter Moon"},
    {"lakota": "Waníyetu Wíčhokaŋ Wi", "english": "The 13th Moon"}
]

# Starting point: First full moon of 2025
current_date = datetime(2025, 1, 13)

print(f"{'#':<3} | {'Lakota Name':<25} | {'Dates (Approximate)'}")
print("-" * 60)

for i, moon in enumerate(lakota_moons):
    end_date = current_date + timedelta(days=29)
    print(f"{i+1:02} | {moon['lakota']:<25} | {current_date.strftime('%b %d')} to {end_date.strftime('%b %d')}")
    # Fix: Indent this line so the date updates for every moon
    current_date = end_date + timedelta(days=1)
