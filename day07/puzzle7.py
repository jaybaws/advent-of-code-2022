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
            _, _, dir = line.strip().split()

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
            file_size, file_name = line.strip().split()
            file = File(name=file_name, size=file_size)
            current_dir.addFile(file)

print(sum([dir.total_size() for dir in directories if dir.total_size() <= 100000]))

total_space_used = root_directory.total_size()
free_space = 70000000 - total_space_used 
desired_cleanup_space = 30000000 - free_space

print(min([dir.total_size() for dir in directories if dir.total_size() >= desired_cleanup_space]))

"""
Right after completion:
- MOTHERFUCKER!
- Made it too difficult on myself: had expected that this program would return in next puzzels.
  Figured It'd probably be smart of use classes. Decided to try @dataclasses. Ran into loads of shit:
  - Sets of dataclassses need a hash() function.
  - Could not import __future__ annotations...
    - Had to upgrade python version
- Annoyed that I couldn't get the (recursive) __repr__ to properly print the full path...
- Annoyed that I made a partial linked-list instead of something 'functional'
Right after seeing other people's solutions:
- Dang it. Great to see I come from a different background (not a data guy).
  - Loved the approach where others increase the folder size of all (intermediat) folders! Smarter algorithm!
Learned:
- OOP
- @dataclasses
  - Factories on mutable properties of @dataclasses
- Missed opportunities:
  - using annotations to signal what should be used for a hash()
- Started using type hints! Those are nice/good!
"""