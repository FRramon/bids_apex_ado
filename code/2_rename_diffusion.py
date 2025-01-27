# rules are : for dwi files in the folder dwi, 
#	if acq is custom : 
	# check PhaseEncodingDirection:
		# if custom + j : acq-30dirs_dir-PA
		# if custom + j- : acq-30dirs_dir-AP
# 	if acq == orig:
		# if orig + j : acq-32dirs_dir-PA
		# No orig is j- --> end

# for all fmap/dir-AP_epi*
	# check PhaseEncodingDirection:
		# if  j : acq-6dirs_dir-PA
		# if  j- : acq-6dirs_dir-AP
#end

import os
import glob
import nibabel as nib
import subprocess
import json
import pandas as pd
from tqdm import tqdm 

rename_custom = False
rename_orig = False
rename_fmap = False

rename_option = False

df_rename_info = pd.DataFrame(columns=["original_filename", "new_filename"])
rename_data = []

bids_dir = "/Volumes/CurrentDisk/APEX/apex_data/rawdata_bids"

##### dwi custom  Orig has 3 b = 0 s/mm2, 30 b = 1500 s/mm2
if rename_custom:
	print("rename dwi custom to dwi 30 dirs")
	custom_acq = glob.glob(os.path.join(bids_dir,"sub-ado*","*","dwi","*custom*.json"))
	for acq in tqdm(custom_acq):

		list_files = glob.glob(acq[:-5] + "*") ### get the list of files (bvec, bval, nii, json) associated with the json

		with open(acq, 'r',encoding = "utf-8") as infile:
			json_data = json.load(infile)

			# PhaseEncodingDirection is j when PA, j- when AP (for GE machines)

			if json_data["PhaseEncodingDirection"] == "j":
				updated_files = [s.replace('acq-custom', 'acq-30dirs_dir-PA') for s in list_files] # replace custom by 30dirs_dir-PA
			elif json_data["PhaseEncodingDirection"] == "j-":
				updated_files = [s.replace('acq-custom', 'acq-30dirs_dir-AP') for s in list_files] # replace custom by 30dirs_dir-AP

		for i,file in enumerate(list_files):

			new_filename = updated_files[i]
			rename_data.append({"original_filename": file, "new_filename": new_filename})
			if rename_option:
				os.rename(file,new_filename)



##### dwi orig. Orig has 1 b = 0 s/mm2, 32 b = 1500 s/mm2

if rename_orig: 
	print("rename dwi orig to dwi 32 dirs")

	orig_acq = glob.glob(os.path.join(bids_dir,"sub-ado*","*","dwi","*orig*.json"))
	for acq in tqdm(orig_acq):
		list_files = glob.glob(acq[:-5] + "*")

		with open(acq, 'r',encoding = "utf-8") as infile:
			json_data = json.load(infile)

			if json_data["PhaseEncodingDirection"] == "j":
				updated_files = [s.replace('acq-orig', 'acq-32dirs_dir-PA') for s in list_files] # replace custom by 32dirs_dir-PA

			elif json_data["PhaseEncodingDirection"] == "j-":
				updated_files = [s.replace('acq-orig', 'acq-32dirs_dir-AP') for s in list_files] # replace custom by 32dirs_dir-PA

		for i,file in enumerate(list_files):

			new_filename = updated_files[i]
			rename_data.append({"original_filename": file, "new_filename": new_filename})
			if rename_option:
				os.rename(file,new_filename)


##### fmap AP

if rename_fmap:
	print("rename fmap to dwi")
	ap_acq = glob.glob(os.path.join(bids_dir,"sub-ado*","*","fmap","*AP*.json"))
	for acq in tqdm(ap_acq):

		list_files = glob.glob(acq[:-5] + "*")

		with open(acq, 'r',encoding = "utf-8") as infile:
			json_data = json.load(infile)

			#print(json_data["PhaseEncodingDirection"])

			if json_data["PhaseEncodingDirection"] == "j":
				updated_files = [s.replace('dir-AP_epi', 'acq-6dirs_dir-PA_dwi') for s in list_files] # replace custom by 32dirs_dir-PA
				updated_files = [s.replace('fmap', 'dwi') for s in updated_files] # replace custom by 32dirs_dir-PA

				print(updated_files)
			elif json_data["PhaseEncodingDirection"] == "j-":
				updated_files = [s.replace('dir-AP_epi', 'acq-6dirs_dir-AP_dwi') for s in list_files] # replace custom by 32dirs_dir-PA
				updated_files = [s.replace('fmap', 'dwi') for s in updated_files] # replace custom by 32dirs_dir-PA

		for i,file in enumerate(list_files):

			new_filename = updated_files[i]
			rename_data.append({"original_filename": file, "new_filename": new_filename})
			if rename_option:
				os.rename(file,new_filename)


# df_rename_info = pd.DataFrame(rename_data)
# df_rename_info.to_csv("/Volumes/CurrentDisk/APEX/apex_data/rename_infos.csv", index=False)

old_fmap_list = glob.glob(os.path.join(bids_dir,"sub-ado*","*","fmap","*"))
for old_fmap in old_fmap_list:
	print(old_fmap)
	#os.remove(old_fmap)
























