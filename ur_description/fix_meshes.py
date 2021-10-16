import pymeshlab as ml
import glob
import os

cur_dir = os.getcwd()
print(cur_dir)

for f in glob.glob(cur_dir + "/meshes/**/*.dae", recursive=True):
    ms = ml.MeshSet()
    # Load then save again
    ms.load_new_mesh(f)
    ms.save_current_mesh(f)



