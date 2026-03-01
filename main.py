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
