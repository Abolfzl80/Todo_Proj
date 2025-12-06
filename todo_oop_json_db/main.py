from Task import Task

dd = Task()

print(dd.add_new_task("read book", "reading book for 2H", "1404.9.1"))
print(dd.add_new_task("play game", "play cs2 for 3H", "1404.8.20"))
print(dd.add_new_task("asleep", "just sleep:)", "1404.8.21"))

print(dd.all_tasks())
print(dd.dele_task("play game"))
dd.show_not_finished_task()
print(dd.finish_task("play game"))