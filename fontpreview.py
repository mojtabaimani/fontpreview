import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from bidi.algorithm import get_display
import arabic_reshaper

# For latin sentence
sentence = "The quick brown fox jumps over the lazy dog"

# For Persian sentence
# reshaped_text = arabic_reshaper.reshape('پاراگراف آزمایشی برای تست')
# Apply bidi algorithm to get the correct display order
# sentence = get_display(reshaped_text)


# Set the font size
font_size = 18  # Set a default font size

# Specify the path to the Verdana font on your system
# This is an example path; you'll need to adjust it based on where Verdana is located on your machine
verdana_font_path = '/Users/mojtaba/tmp/pn.ttf'  # Adjust this path
verdana_font_prop = font_manager.FontProperties(fname=verdana_font_path, size=font_size)

fonts_list = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')

fig_height = len(fonts_list) * 0.3 + 1
fig_width = 8

plt.figure(figsize=(fig_width, fig_height))
ax = plt.gca()
ax.axis('off')

for index, font_path in enumerate(fonts_list):
    try:
        font_name = font_manager.FontProperties(fname=font_path).get_name()
        y_position = 1 - (index + 1) * 0.4 / fig_height
        # Render the sentence in the system font
        ax.text(0.50, y_position, sentence, fontsize=font_size, fontproperties=font_manager.FontProperties(fname=font_path), transform=ax.transAxes)
        # Render the font name in Verdana
        ax.text(0.01, y_position, font_name, fontsize=font_size, fontproperties=verdana_font_prop, transform=ax.transAxes)
    except Exception as e:
        print(f"Skipping font at path {font_path} due to error: {e}")
        continue

plt.savefig("all_fonts_image.png", bbox_inches='tight')
plt.close()
