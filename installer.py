from pathlib import Path
from traceback import format_exc
import json
import shutil

from tkinter import messagebox#, Tk
# from tkinter.ttk import Progressbar


def main():
    with open("install_config.json") as f:
        config = json.load(f)

    # start = 0
    # bar = Tk()
    base_path = Path("./")
    for i, step in enumerate(config):
        if step["type"] == "start":
            if "base_path" in step: base_path = Path(step["base_path"])

            if "title" in step: title: str = step["title"]
            else: title = "Installer"

            if "message" in step: message: str = step["message"]
            else: message = "Application will be installed at \"{base_path}\", proceed?"
            message = message.format(base_path=base_path)

            if not messagebox.askokcancel(title=title, message=message): break

        elif step["type"] == "folder":
            source = Path(step["folder"])
            dest = base_path / Path(step["dest"])
            if "whole" in step and step["whole"] and dest.name != source.name:
                dest /= source.name
            print("source", source)
            print("dest", dest)
            print("result", shutil.copytree(source, dest, dirs_exist_ok=True))

        elif step["type"] == "file":
            source = Path(step["file"])
            dest = base_path / Path(step["dest"])
            dest /= source.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            print("source", source)
            print("dest", dest)
            print("result", shutil.copyfile(source, dest))

        elif step["type"] == "end":
            if "message" in step: message = step["message"]
            else: message = "Application succesfully installed!"

            messagebox.showinfo(title="Succes", message=message)
            break


if __name__ == "__main__":
    try:
        main()
    except PermissionError as e:
        messagebox.showerror(
            title="Missing permission",
            message="This installation process requires administrator permissions, please run as administrator."
        )
    except Exception as e:
        messagebox.showerror(title="Error", message=format_exc())
