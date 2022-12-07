from typing import Set
from directory import Directory
from file import File

input = open('input.txt', 'r')
lines = input.readlines()

root_directory = Directory(name='/')
current_dir = root_directory

directories: Set[Directory] = set() 
directories.add(root_directory)

for line in lines:
    if line.startswith('$'):
        if line.startswith('$ cd'):
            dir = line.strip().split()[2]

            if dir == '/':
                current_dir = root_directory
            elif dir == '..':
                current_dir = current_dir.parent
            else:
                new_dir = Directory(name=dir, parent=current_dir)
                current_dir.addDir(new_dir)
                directories.add(new_dir)
                current_dir = new_dir

        elif line.startswith('$ ls'):
            pass
        else:
            pass
    else:
        if line.startswith('dir'):
            pass  # Don't care; we'll add the dir once we 'cd' into it
        else:
            file_name = line.strip().split()[1]
            file_size = line.strip().split()[0]
            file = File(name=file_name, size=file_size)
            current_dir.addFile(file)

print(sum([dir.total_size() for dir in directories if dir.total_size() <= 100000]))

total_space_used = root_directory.total_size()
free_space = 70000000 - total_space_used 
desired_cleanup_space = 30000000 - free_space

print(min([dir.total_size() for dir in directories if dir.total_size() >= desired_cleanup_space]))