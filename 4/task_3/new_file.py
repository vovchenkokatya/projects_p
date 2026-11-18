import sys
from pathlib import Path
from colorama import Fore, Style, Back

print(Back.BLUE + Fore.BLACK + Style.BRIGHT + f"{sys.argv}" + Style.RESET_ALL)
# current_dir = Path(__file__).parent
# if current_dir.exists():
#     if current_dir.is_dir():
#         print(Fore.RED + f"{current_dir.name}")

if len(sys.argv) != 2:
    sys.exit(1)

path = Path(sys.argv[1])

for name in sorted(path.rglob("*")):
    if ".venv" in name.relative_to(path).parts:      # тут я вирішила не друкувати файли з збірки вірт. сер.
        continue
    if name.is_dir():
        print(Fore.RED + name.name)
    else:
        files_space = " " * 4                        # пробіли просто для зрозумілості виводу (файли у папці)
        print(Fore.GREEN + files_space + name.name)