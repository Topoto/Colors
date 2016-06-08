#Scripts from Blender Build scripts; svn.blender.org/svnroot/bf-blender/trunk/blender/build_files/scons/tools/bcolors.py
#Reorginized by Merkie; github.com/Merkie

class colors:
    PINK = '\033[95m'
    PURPLE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLACK = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print colors.PINK + "Pink!" + colors.BLACK
print colors.PURPLE + "Purple!" + colors.BLACK
print colors.GREEN + "Green!" + colors.BLACK
print colors.YELLOW + "Yellow!" + colors.BLACK
print colors.RED + "Red!" + colors.BLACK
print colors.BLACK + "Black!" + colors.BLACK
print colors.BOLD + "Bold!" + colors.BLACK
print colors.UNDERLINE + "Underlined!" + colors.BLACK

