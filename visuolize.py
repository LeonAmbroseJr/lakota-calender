import matplotlib.pyplot as plt
import numpy as np

# Moon data with colors to represent seasons
lakota_moons = [
    {"name": "Wiótheȟika Wi", "color": "white"},
    {"name": "Čhaŋnápopa Wi", "color": "silver"},
    {"name": "Ištáwičhayazan Wi", "color": "skyblue"},
    {"name": "Maǧá Okáda Wi", "color": "lightgreen"},
    {"name": "Wóžupi Wi", "color": "green"},
    {"name": "Wípazuka Wasté Wi", "color": "red"},
    {"name": "Čhaŋpȟásapa Wi", "color": "darkred"},
    {"name": "Wasútȟuŋ Wi", "color": "gold"},
    {"name": "Čhaŋwápeǧi Wi", "color": "orange"},
    {"name": "Čhaŋwápekasna Wi", "color": "brown"},
    {"name": "Waníyetu Wi", "color": "darkblue"},
    {"name": "Waníčhokaŋ Wi", "color": "navy"},
    {"name": "Waníyetu Wíčhokaŋ Wi", "color": "blue"}
]

# Set up the circular plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})

# Divide the circle into 13 segments
n_moons = len(lakota_moons)
theta = np.linspace(0, 2 * np.pi, n_moons, endpoint=False)
width = (2 * np.pi) / n_moons

# Create the bars for each moon
bars = ax.bar(theta, [1]*n_moons, width=width, bottom=0.5, 
               color=[m['color'] for m in lakota_moons], edgecolor='black', alpha=0.7)

# Add the Lakota names as labels
ax.set_xticks(theta)
ax.set_xticklabels([m['name'] for m in lakota_moons], fontsize=10, fontweight='bold')

# Clean up the visual
ax.set_yticklabels([])
ax.set_theta_zero_location('N') # Start at the top
ax.set_theta_direction(-1)     # Go clockwise
plt.title("Lakota 13-Moon Sacred Calendar", size=15, pad=20)

plt.show()
