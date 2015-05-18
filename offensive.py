import os
from sys import argv

script, foldername = argv

has_init_method = False
method_lines = []
has_offensive_classes = False

for path, subfolders, files in os.walk(foldername):    
    for filename in files:
        extension = os.path.splitext(filename)[1]    
        if extension == ".m":
            f = open(os.path.join(path,filename), "r")

            lines = [line for line in f if line.strip()]

            for line in lines:
                if line.startswith("- (") or line.startswith("-("):
                    if ")init" in line or ") init" in line:
                        has_init_method = True
                    else:
                        method_lines.append(line)
                    
            method_count = len(method_lines)
            if has_init_method and method_count == 1:
                has_offensive_classes = True
                print "You have an offensive class: %s" % filename
            f.close()
        
if not has_offensive_classes:
    print "Congratulations, you do not have any offensive classes!"