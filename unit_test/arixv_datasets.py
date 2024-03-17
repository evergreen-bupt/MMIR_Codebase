"""
arixv_datasets.py

dataset based on sciMMIR ,contains tittle author and figure
We currently only support Map-style Datasets; assumes that all files (annotations, images) are on local disk, and that
random access image reading is relatively cheap/fast.
"""
import copy
import json
from pathlib import Path
from typing import Dict, List, Tuple, Type

import torch
from PIL import Image
from torch.utils.data import Dataset
# from transformers import LlamaTokenizerFast, PreTrainedTokenizerBase
# from prismatic.models.backbones.vision import ImageTransform
import datasets
IGNORE_INDEX = -100


def load_json(path):
    f = open(path , 'r')
    data = json.load(f)
    f.close()

    return data

class ArixvDataset(Dataset[Dict[str, torch.Tensor]]):
    def __init__(
        self,
        mode: str,
        # data_path: str,
        # fig_path: str,
        # text_2_image_index: str,
        # text_2_index: str,
        # config,
    ):
        super(ArixvDataset , self).__init__()
        # process = DataProcess()
        self.mode = mode
        # self.data_path = data_path
        # self.fig_path = fig_path
        # self.text_2_image_index = load_json(text_2_image_index)
        # self.text_2_index = load_json(text_2_index)
        # self.config = config
        ds_remote = datasets.load_dataset("yizhilll/SciMMIR_dataset", cache_dir = '/ML-A100/team/mm/xw/models/hub')

        if mode == 'test':
            # self.examples = process.get_test_samples(data_path, mode, self.fig_file_name_2_index , self.text_2_index, self.config.image_type )
            self.examples = ds_remote['test']
            # logging.info("Current examples: %s" , len(self.examples))


        # logging.info("Current examples: %s" , len(self.examples))

    def __getitem__(self, index):
        example = self.examples[index]
        Query = example['text']
        Fig = example['image']
        # Fig = Image.open(f"{self.fig_path}{Fig}")
        # Fig_num = self.text_2_image_index[Query]
        # Text_num = self.text_2_index[Query]
        Image_type = example['class']

        return {
            # 'Fig_num': Fig_num,
            # 'Text_num': Text_num,
            "Image_type": Image_type
        }

    def __len__(self):
        return len(self.examples)