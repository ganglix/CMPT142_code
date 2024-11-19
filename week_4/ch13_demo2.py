# nested dictionary

# green colour theme for a website
green_theme = {
    "background": {"red": 0, "green": 100, "blue": 0},
    "foreground": {"red": 0, "green": 200, "blue": 100},
    "font": {"red": 255, "green": 255, "blue": 255}
}
# halve all of the green intensities (round down to nearest int)

# for component in green_theme:
#     color_setting = green_theme[component]
#     # color_setting {color: intensity}
#     color_setting["green"] //= 2   # color_setting["green"] = color_setting["green"] //2
#
# print(green_theme)

# green_theme['background']['green']   # green intesity (100) of "background" component

for k in green_theme:
    value_sub_dict = green_theme[k]
    print(value_sub_dict)
    # color_setting {color: intensity}
    value_sub_dict["green"] //= 2   # color_setting["green"] = color_setting["green"] //2

# print(green_theme)
