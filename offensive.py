import os
from sys import argv

script, foldername = argv

offending_classes = []

# This is a blacklist of NSObject methods that should not be accounted for in determining if a class is offensive or not. 
# If you're subclass only needs a description, you're doing it wrong.
blacklist = ["-(NSString*)description{", "-(BOOL)isEqual:", "-(NSUInteger)hash", "-(NSString)debugDescription", ")copyWithZone:(NSZone*)zone"]

for path, subfolders, files in os.walk(foldername):   
    for filename in files:
        has_init_method = False 
        whitelisted_methods = []
        
        extension = os.path.splitext(filename)[1]    
        if extension == ".m":
            f = open(os.path.join(path,filename), "r")
            lines = [line for line in f if line.strip()]

            for line in lines:
                l = line.replace(' ', '')
                if l.startswith("-("):
                    if ")init" in l:
                        has_init_method = True
                    else:
                        matched = False
                        for black in blacklist:
                            if black in l:
                                matched = True

                        if not matched:
                            whitelisted_methods.append(line)
            
            method_count = len(whitelisted_methods)
            if has_init_method and method_count <= 1:
                offending_classes.append(filename)
            f.close()
        
if len(offending_classes) > 0:
    for classname in offending_classes:
        print classname
else:
    print "Congratulations, you do not have any offensive classes!"