import os
import tqdm
import glob
import time

# This script monitors for pictures in the Downloads folder and move the pictures into the Pictures/wallpaper folder

os.chdir("/home/akame/Downloads")
file_list = os.listdir()
final_destination = os.path.join("~", "Pictures/wallpaper/")
dst_length = len(os.listdir("../Pictures/wallpaper/"))

# version 1

# for x in file_list:
#     if ".jpg" in x or ".png" in x :
#        

#         # check for spaces in the name
#         if " " in x:
#             arr = x.split(" ")
#             name = f"{arr[0]}{dst_length}.jpg"

#             # rename original file, making it easier to move
#             os.rename(x, name)
        
#         if os.path.exists(f"{final_destination}{name}") :
#             raise Exception("File already exists")
#         else:
#             try:
#                 os.system(f"mv {name} {final_destination}")
#             except Exception :
#                 print(Exception)
            
#             print(f"Moved {name}")


# version 2
pbar = tqdm.tqdm(glob.glob("*.jpg"), smoothing=0.5)

for x in pbar:
    pbar.set_description(x)
    name = x
    dst_length += 1

    #  check for spaces in the name
    if " " in x:
        arr = x.split(" ")
        name = f"{arr[0]}{dst_length}.jpg"

        # rename original file, making it easier to move
        os.rename(x, name)
    
    if os.path.exists(f"{final_destination}{name}") :
        raise Exception("File already exists")
   
    try:
        os.system(f"mv {name} {final_destination}")
    except Exception :
        print(Exception)

    time.sleep(0.5)

print("Photos Moved")


# version 3 (recursion) 
# pbar = tqdm.tqdm(glob.glob("*.jpg"), smoothing=0.5)
# length = len(pbar)
# final_destination = os.path.join("~", "Pictures/wallpaper/")
# dst_length = len(os.listdir("../Pictures/wallpaper/"))

# counter = 0
# def recurphotos(dst_length, pbar, final_destination, length) :
#     if counter == dst_length:
#         print("Photos Moved")
#         return

#     else:
#         name = pbar[counter]
#         dst_length += 1

#         #  check for spaces in the name
#         if " " in name:
#             arr = name.split(" ")
#             name = f"{arr[0]}{dst_length}.jpg"

#             # rename original file, making it easier to move
#             os.rename(name, name)
        
#         if os.path.exists(f"{final_destination}{name}") :
#             raise Exception("File already exists")
    
#         try:
#             os.system(f"mv {name} {final_destination}")
#         except Exception :
#             print(Exception)

#         time.sleep(0.5)
#         recurphotos()

# recurphotos(dst_length, pbar, final_destination, length)