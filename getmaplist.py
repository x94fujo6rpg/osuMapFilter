import os
import json
import codecs
from tkinter import Tk, messagebox


def get_list(path):
    map_path = path + "/Songs"
    new_list = []
    for (_, dir_names, _) in os.walk(map_path):
        for names in dir_names:
            if names[0].isdigit():
                new_name = names[0:names.find(" ")]
                new_list.append(new_name)
        return new_list


window = Tk()
window.withdraw()
osu_path = os.getcwd()
isfile = os.path.isfile(osu_path + "/osu!.exe")

if isfile:
    map_list = get_list(osu_path)
    code = "utf-8"
    new_file = "map_list.txt"
    mode = 'w' if os.path.exists(new_file) else 'x'
    with codecs.open(new_file, mode, code) as file:
        json.dump(map_list, file, indent=0, ensure_ascii=False)
    messagebox.showinfo("Done", "Successfully make map_list.txt")
else:
    messagebox.showerror("Error", "Wrong path")
quit()
