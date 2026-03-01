import time
import win32com.client as win
def get_open_explorer_paths():
    shell = win.Dispatch("Shell.Application")
    paths = []
    for window in shell.Windows():
        try:
            path = window.Document.Folder.Self.Path
            paths.append(path)
        except:
            pass
    return paths

def check_dir(path):
        try:
            with open(f"{path}/autorun.run") as f:
                return f.read()
        except FileNotFoundError:
            return None
prev_path = None
x = 0

while True:
    paths = get_open_explorer_paths()
    curr_path = paths[0] if paths else None

    if curr_path != prev_path:
        prev_path = curr_path
        x = 0

    if x == 0 and curr_path:
        content = check_dir(curr_path)
        if content:
            exec(content)
        x += 1

    time.sleep(1)

