import os
import time
os.system("clear")
print("[                    ] 0% " )
time.sleep(1)
print("[=====➣              ] 25%")
time.sleep(1)
print("[==========➣         ] 50%")
time.sleep(1)
print("[===============➣     ] 75%")
time.sleep(1)
print("[====================✔] 100%")
time.sleep(1)
os.system("clear")
class color:
	RED = '\033[91m'
	YELLOW = '\033[93m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	END = '\033[0m'


print (color.RED +     """
$$$$$$$$$$$$$$$$$$$
$                 $         
$     virus450    $
$                 $  
$     Find even   $
$    odd numbers  $
$$$$$$$$$$$$$$$$$$$
""" + color.END)

add =input(color.YELLOW +'\n The desired number >>>' + color.END)
add = int(add)
if (add % 2) == 0:
	os.system("clear")
	print(color.BLUE + "Is an even number" + color.END)
	
else:
	os.system("clear")
	print(color.BLUE + "Is an odd number" + color.END)
