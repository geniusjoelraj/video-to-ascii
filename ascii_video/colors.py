# intensity_max = "\033[0;30m"
# intensity_low = "\033[0;37m"
# intensity_medium = "\033[1;30m"
# light_white = "\033[1;37m"
# white=""
#
# colors = [intensity_max, intensity_medium, intensity_low, light_white, light_white, white]

end = "\033[0m"
def rgb_to_ansi(rgb):
    r, g, b=rgb
    return f"\x1b[38;2;{r};{g};{b}m"
# def rgb_to_ansi(rgb):
#     r, g, b = rgb
#     if r < 50 and g < 50 and b < 50:
#         return "\033[0;30m"  # BLACK
#     elif r > 200 and g < 100 and b < 100:
#         return "\033[0;31m"  # RED
#     elif r < 100 and g > 200 and b < 100:
#         return "\033[0;32m"  # GREEN
#     elif r > 150 and g > 100 and b < 50:
#         return "\033[1;33m"  # YELLOW
#     elif r < 100 and g < 100 and b > 200:
#         return "\033[0;34m"  # BLUE
#     elif r > 150 and g < 100 and b > 150:
#         return "\033[0;35m"  # PURPLE
#     elif r < 100 and g > 150 and b > 150:
#         return "\033[0;36m"  # CYAN
#     elif r > 200 and g > 200 and b > 200:
#         return "\033[1;37m"  # LIGHT WHITE
#     elif r > 150 and g > 150 and b > 150:
#         return "\033[0;37m"  # LIGHT GRAY
#     elif r > 100 and g < 100 and b < 100:
#         return "\033[1;31m"  # LIGHT RED
#     elif r < 100 and g > 100 and b < 100:
#         return "\033[1;32m"  # LIGHT GREEN
#     elif r < 100 and g < 100 and b > 100:
#         return "\033[1;34m"  # LIGHT BLUE
#     elif r > 150 and g < 100 and b > 100:
#         return "\033[1;35m"  # LIGHT PURPLE
#     elif r < 100 and g > 100 and b > 100:
#         return "\033[1;36m"  # LIGHT CYAN
#     elif r > 100 and g > 100 and b < 100:
#         return "\033[0;33m"  # BROWN
#     else:
#         return "\033[1;30m"  # DARK GRAY (fallback)
#
