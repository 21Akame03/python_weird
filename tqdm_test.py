# import time
# import tqdm 

# for i in tqdm.tnrange(100):
#     time.sleep(1)

# print("done")


import time
from tqdm import tqdm

for i in tqdm(range(100)):
    time.sleep(0.1)

print("done!")