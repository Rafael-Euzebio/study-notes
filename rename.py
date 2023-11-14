import os
path =  os.getcwd()
import re

ignored = ['.gitignore', '.git', '.obsidian']
folders = [x for x in os.listdir(path) if x not in ignored]

def rename():
    for dir, subdir, listfilename in os.walk(path):
        subdir[:] = [d for d in subdir if d not in ignored]
        for folder in subdir:
            new_name = folder.replace('_', '-', 2)
            os.rename(os.path.join(dir, folder), os.path.join(dir, new_name))

def links():
    for dir, subdir, listfilename in os.walk(path):
        subdir[:] = [d for d in subdir if d not in ignored]
        for filename in listfilename:
            with open(os.path.join(dir, filename)) as file:
                filedata = file.read()
                matches = re.findall('\[\[.*?\]\]', filedata)
                for match in matches:
                    new_string = match.replace("-", "_", 1)
                    filedata = filedata.replace(match, new_string)

                    with open(os.path.join(dir, filename), 'w') as write_file:
                        write_file.write(filedata)

def markdown():
    for dir, subdir, listfilename in os.walk(path):
        subdir[:] = [d for d in subdir if d not in ignored]
        for filename in listfilename:
            with open(os.path.join(dir, filename)) as file:
                filedata = file.read()
                matches = re.findall('\[.*?\]', filedata)

                for match in matches:
                    new_string = match.replace("-", ' ')
                    filedata = filedata.replace(match, new_string)

                    with open(os.path.join(dir, filename), 'w') as write_file:
                        write_file.write(filedata)

def fuzzy():
    for dir, subdir, listfilename in os.walk(path):
        subdir[:] = [d for d in subdir if d not in ignored]
        for filename in listfilename:
            with open(os.path.join(dir, filename)) as file:
                filedata = file.read()
                matches = re.findall('\(./CS50x.*?\)', filedata)

                for match in matches:
                    new_string = match.replace("CS50x", './CS50x')
                    filedata = filedata.replace(match, new_string)

                    with open(os.path.join(dir, filename), 'w') as write_file:
                        write_file.write(filedata)

fuzzy()
