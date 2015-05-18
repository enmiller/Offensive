# Description
An offensive class is any two-method class where one of the methods is simply `-init`.  These types of classes usually indicate points of refactoring where the class can be eliminated altogether.

This script will traverse the project folder looking for all Objective-C classes ending in `.m` and determines if that class is offensive or not. 

## Usage
In terminal, run the following command using your project's file path:

<pre><code>python offensive.py ~/Documents/myproject/classes</code></pre>

## Issues
- None