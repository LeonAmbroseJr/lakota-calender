# lakota-calender

A Python visualization of the Lakota 13-moon calendar system with astronomical alignment to full moon dates.

## Features

- **Circular Wheel**: Traditional circular calendar layout showing all 13 Lakota moons
- **Linear Strip**: Month-by-month horizontal visualization
- **Lunar Alignment**: Full moon dates for 2025 synced with Lakota moon names and colors

## Lakota Moons (with colors)

1. Magaksicha Agli Wi (Bear Moon) - Brown
2. Chanwaghpeto Wi (Frost Moon) - Silver
3. Istawichunke Wi (Sap Rising Moon) - Sky Blue
4. Magpie Moon - Green
5. Wasunpi Wi (Ripening Moon) - Gold
... and 8 more

## Installation

```bash
pip install matplotlib numpy pandas
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

# Starting point: The first full moon of 2025
current_date = datetime(2025, 1, 13)

print(f"{'#':<3} | {'Lakota Name':<25} | {'Dates (Approximate)'}")
print("-" * 60)

for i, moon in enumerate(lakota_moons):
    end_date = current_date + timedelta(days=29)
    print(f"{i+1:02} | {moon['lakota']:<25} | {current_date.strftime('%b %d')} to {end_date.strftime('%b %d')}")

01 | Wiótheȟika Wi            | Jan 13 to Feb 11
02 | Čhaŋnápopa Wi            | Feb 12 to Mar 13
03 | Ištáwičhayazan Wi        | Mar 14 to Apr 12
...
    current_date = end_date + timedelta(days=1)

