#!/usr/bin/env python3
"""
generate_multimodal_view_config.py
====================================
Generates Vitessce view config for multimodal data from template
"""

import fire
import json

# To use this script:
# python generate_multimodal_view_config.py --template_path ./multimodal_config_templates/integrated_3.json --output_path <path to output JSON file>

# In order to create your own Vitessce Config file, you will want to prepare
# all the relevant Zarr files listed below and those will replaced placeholders
# in the input template file.
dataset_path_dict = {
    "iss": {
        "raw": "https://hindlimb.cog.sanger.ac.uk/datasets/integrated-test/0.0.1/rotated/hindlimb-iss-rotated_90-raw.zarr",
        "label": "https://hindlimb.cog.sanger.ac.uk/datasets/20230419_multimodal/0.0.1/hindlimb-hindlimb_subtype-label.zarr",
        "ad": "https://hindlimb.cog.sanger.ac.uk/datasets/20230412_multimodal/integrated/0.0.1/hindlimb-iss-integrated-rotated_90-anndata.zarr",
    },
    "visium": {
        "raw": "https://hindlimb.cog.sanger.ac.uk/datasets/Visium/0.0.1/Hindlimb_visium_slide_7_raw.zarr",
        "label": "https://hindlimb.cog.sanger.ac.uk/datasets/20230412_multimodal/integrated/0.0.1/hindlimb-visium-integrated-WSSS_THYst9699525-label.zarr",
        "ad": "https://hindlimb.cog.sanger.ac.uk/datasets/20230412_multimodal/integrated/0.0.1/hindlimb-visium-integrated-WSSS_THYst9699525-anndata.zarr",
    },
    "scrnaseq": {
        "ad": "https://hindlimb.cog.sanger.ac.uk/datasets/20230412_multimodal/integrated/0.0.1/hindlimb-scrnaseq-integrated-anndata.zarr"
    },
}


# generate_multimodal_view_config with user input
def generate_multimodal_view_config(
    dataset_path_dict: dict, template_path: str, output_path: str
):
    # read the JSON file
    with open(template_path) as f:
        conf = json.load(f)
    out_conf = conf.copy()
    # update the dataset paths
    for d in out_conf["datasets"]:
        print(d["uid"])
        print(dataset_path_dict[d["uid"]])
        # update the image paths
        for f in d["files"]:
            # check if the file is a json file
            if f["fileType"].endswith("json"):
                for i in f["options"]["images"]:
                    t = i["name"].split("-")[-1]
                    print(t, i["url"])
                    i["url"] = dataset_path_dict[d["uid"]][t]
            else:
                print(f["url"])
                f["url"] = dataset_path_dict[d["uid"]]["ad"]
    # write the output JSON file
    with open(output_path, "w") as f:
        json.dump(out_conf, f)


if __name__ == "__main__":
    fire.Fire(generate_multimodal_view_config)
