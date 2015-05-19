# Description
An offensive class is any two-method class where one of the methods is simply `-init`.  These types of classes usually indicate points of refactoring where the offending class can be eliminated altogether.

This script will traverse the project folder looking for all Objective-C classes ending in `.m` and determines if that class is offensive or not. 

## Usage
In terminal, run the following command using your project's file path:

<pre><code>python offensive.py ~/Documents/myproject/classes</code></pre>

A blacklist has been added to the script that will filter out overrides of specific NSObject methods such as:  
- description  
- debugDescription  
- isEqual  
- hash  

As well as NSCopying's  
- copyWithZone

The choice was made to filter these because those methods, by themselves, should not warrant creating or keeping around an offending class.

## Notes
This script was inspired by an awesome video on why less is more when writing code.  A very insightful [video](https://youtu.be/o9pEzgHorH0 "video").

And a thanks to [larsacus](https://github.com/larsacus) for helping with the script.