import os
from PIL import Image, ImageDraw, ImageFont

color_meaning = {
    "5e5bc5": "Bridge",
    "706419": "Fence",
    "7f4502": "House",
    "8f2a91": "Platform",
    "9600b1": "Roof",
    "aad16a": "Wall-Brick",
    "ae2974": "Wall-Stone",
    "b0c1c3": "Wall-Wood",

    "6e6e28": "Dirt",
    "7c32c8": "Gravel",
    "7d3054": "Ground-other",
    "87716f": "Mud",
    "8b3027": "Pavement",
    "946e28": "Road",
    "999900": "Sand",

    "696969": "Clouds",
    "77ba1d": "Fog",
    "7ec864": "Hill",
    "869664": "Mountain",
    "9364c8": "River",
    "956432": "Rock",
    "9ac6da": "Sea",
    "9ceedd": "Sky",
    "9e9eaa": "Snow",
    "a1a164": "Stone",
    "b1c8ff": "Water",

    "606e32": "Bush",
    "760000": "Flower",
    "7bc800": "Grass",
    "a2a3eb": "Straw",
    "a8c832": "Tree",
    "b57b00": "Wood",
}


def get_path_from_user():
    print("Please input path")
    print("Example: C:\\Users\\user\\OneDrive\\Desktop\\gaugan_test")

    # gets the input from the user
    s = input()
    if os.path.isdir(s):
        # check's whether the input ends on a \ or not, then acts accordingly
        if s.endswith("\\"):
            return s
        else:
            return s + "\\"
    else:

        # this one is pretty obvious
        print("Directory not exists.")


def get_yes_or_no_files_from_user():
    print("Do you want all subdirectories processed? (y/n)")

    # gets the input from the user
    s = input()

    if s == "y":
        return "y"
    elif s == "n":
        return "n"
    else:
        print("Invalid input. Only Current Directory will be processed")
        return "n"


def get_width_from_user():
    print("Please input the width you want your image to have in pixel")
    print("Example: 1000 is nice and crisp.")

    # gets the input from the user
    try:
        s = int(input())
        return s
    except:
        print("Invalid input. Try again")
        return get_width_from_user()


def draw_text(x, y, text, d):
    font = font = ImageFont.truetype("arialbd.ttf", fontsize)

    # set the colors for text and outline
    shadow_color = (255, 255, 255)
    text_color = (000, 000, 000)

    # border
    d.text((x - shadow, y - shadow), text, font=font, fill=shadow_color)
    d.text((x + shadow, y - shadow), text, font=font, fill=shadow_color)
    d.text((x - shadow, y + shadow), text, font=font, fill=shadow_color)
    d.text((x + shadow, y + shadow), text, font=font, fill=shadow_color)

    # now draw the text over it
    d.text((x, y), text, font=font, fill=text_color)


def draw_box(x, y, color, d):
    # draw a rectangle x and y mark the starting coordinates
    d.rectangle([(x, y), (x + width, y + height)], fill="#" + color)


def get_list_of_text_names(path):
    # assign directory
    # directory = 'C:\\Users\\brabb\\OneDrive\\Desktop\\gaugan_test'

    list_of_text_names = []

    # iterate over files in
    # that directory
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        # checking if it is a file
        if os.path.isfile(f) and f.endswith(".txt"):
            list_of_text_names.append(filename)

    return list_of_text_names


def generate_color_lists(path):
    f = open(path)
    s = []
    for line in f:
        for col_code in line.strip().split(','):
            s.append(str(col_code))
    f.close()
    return s


def generate_list_of_images(path, list_of_names):
    for i in list_of_names:
        generate_image(path + i)


def generate_image(path):
    print("working on: " + path)
    color_list = generate_color_lists(path)
    i = len(color_list)
    """
    width_n = int((i/3)*2)
    length_n = int((1/3))
    """
    img = Image.new('RGB', (width, (height + (height * (i - 1)))), color=(000, 000, 000))

    count = 1
    for j in color_list:
        try:
            d = ImageDraw.Draw(img)
            draw_box(0, (0 + (height * (count - 1))), j, d)
            draw_text(text_distance, (text_distance + (height * (count - 1))), color_meaning.get(j), d)
            count = count + 1
            img.save(path[:-4] + "_legend.png")
        except:
            try:
                d = ImageDraw.Draw(img)
                draw_box(0, (0 + (height * (count - 1))), j, d)
                draw_text(2, (text_distance + (height * (count - 1))), "unknown: #" + j, d)
                count = count + 1
                img.save(path[:-4] + "_legend.png")
            except:
                try:
                    d = ImageDraw.Draw(img)
                    draw_box(0, (0 + (height * (count - 1))), j, d)
                    draw_text(2, (text_distance + (height * (count - 1))), "unknown: #" + j, d)
                    count = count + 1
                    img.save(path[:-4] + "_legend.png")
                except:
                    d = ImageDraw.Draw(img)
                    draw_box(0, (0 + height), "FFFFFF", d)
                    draw_text(2, (text_distance + height), "unknown: #" + j, d)
                    count = count + 1
                    img.save(path[:-4] + "_legend.png")


if __name__ == '__main__':

    width = get_width_from_user()
    height = int(width / (100 / 30))
    text_distance = width / 10
    fontsize = int(width / 10)
    shadow = width / 250

    my_path = get_path_from_user()

    yes_or_no_files = get_yes_or_no_files_from_user()

    if yes_or_no_files == "y":
        for subdir, dirs, files in os.walk(my_path):
            generate_list_of_images(subdir + os.sep, get_list_of_text_names(subdir + os.sep))
    else:
        generate_list_of_images(my_path, get_list_of_text_names(my_path))