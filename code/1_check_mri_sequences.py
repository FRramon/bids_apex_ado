import os
import glob
import nibabel as nib
import subprocess
import json

bids_dir = "/Volumes/CurrentDisk/APEX/apex_data/rawdata"

custom_acq = glob.glob(os.path.join(bids_dir,"sub-ado*","*","dwi","*custom*.nii.gz"))
orig_acq = glob.glob(os.path.join(bids_dir,"sub-ado*","*","dwi","*orig*.nii.gz"))

print(len(custom_acq))
print(len(orig_acq))


# for acq in custom_acq:

# 	print(acq)

# 	n_img = nib.load(acq)
# 	header = n_img.header
# 	dims = header['dim']

# 	print(dims)

	# subprocess.run(f"mrinfo {acq}",shell = True)

# for acq in orig_acq[:1]:

# 	print(acq)

# 	n_img = nib.load(acq)
# 	header = n_img.header
# 	dims = header['dim']

# 	print(dims)

# custom_acq = glob.glob(os.path.join(bids_dir,"sub-ado*","*","dwi","*custom*.json"))
# orig_acq = glob.glob(os.path.join(bids_dir,"sub-ado*","*","dwi","*orig*.json"))


# for acq in custom_acq:
# 	with open(acq, 'r',encoding = "utf-8") as infile:


# 		json_data = json.load(infile)

# 		if json_data["PhaseEncodingDirection"] != "j":
# 			print(acq)


# 			print(json_data["PhaseEncodingDirection"])

ap_acq = glob.glob(os.path.join(bids_dir,"sub-ado*","*","fmap","*AP*.nii.gz"))
print(len(ap_acq))

for acq in ap_acq:
	n_img = nib.load(acq)
	header = n_img.header
	dims = header['dim']
	print(dims)

ap_acq = glob.glob(os.path.join(bids_dir,"sub-ado*","*","fmap","*AP*.json"))
print(len(ap_acq))

for acq in ap_acq:
	with open(acq, 'r',encoding = "utf-8") as infile:
		json_data = json.load(infile)

		#print(json_data["PhaseEncodingDirection"])

		if json_data["PhaseEncodingDirection"] == "j":
		 	print(acq)
