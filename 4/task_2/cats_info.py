from pathlib import Path

cats_list = []

def get_cat_info(path):

    get_from = Path(path)

    try:
        with open(get_from, "r", encoding="utf-8") as cats:
            cat = [el.strip() for el in cats.readlines()]
            for one in cat:
                id, name, age = one.split(",")
                # print(f"cat id: {id}, cat\'s name: {name}, age: {age}")
                dict_of_cats = {"id": id, "name": name, "age": age}
                cats_list.append(dict_of_cats)
        print(cats_list)

    except FileNotFoundError:
        print("File doesn\'t exist")

