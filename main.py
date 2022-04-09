from watchdog.observers import Observer
import shutil
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            file = folder_track + "/" + filename
            type = filename.split('.')[1]
            if type == 'txt':
                folder_dest_final = folder_dest_txt
            else:
                folder_dest_final = folder_dest

            new_path = folder_dest_final + "/" + filename
            shutil.move(file, new_path)


folder_track = 'C:/Users/sisai/Desktop/Downloads'
folder_dest = 'D:/FromDesktop'
folder_dest_txt = 'D:/FromDesktop/txt'

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while (True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
