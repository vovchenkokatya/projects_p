from pathlib import Path

def total_salary(path) -> tuple:
    current = Path(path)
    sorted_info = Path(__file__).parent / "info.txt"

    count_sal = 0
    people = 0
    try:
        with open(current, "r") as names_file:
            name = [el.strip() for el in names_file.readlines()]
            for person in name:
                empl_name, salary = person.split(",")
                count_sal += int(salary)
                people += 1
                if people == 0:
                    return 0, 0
            # print(count_sal, people)
        # return count_sal, count_sal / people

        with open(sorted_info, "w") as information:
            information.write(f"Overall: {count_sal}\nAverage: {count_sal/people}")

    except FileNotFoundError:
        print("File doesn\'t exist")
        return 0, 0

    try:
        with open(sorted_info, "r") as read:
            text_file = [el.strip() for el in read.readlines()]
            return tuple(text_file)

    except FileNotFoundError:
        print("File doesn\'t exist")