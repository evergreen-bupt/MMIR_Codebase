import sys 
sys.path.append('.')
from unit_test.arixv_datasets import ArixvDataset

dataset=ArixvDataset(
                mode = 'test',
                # data_path = data_path,
                # fig_path = fig_path,
                # text_2_image_index = f"{self.config.LLM_text_embedding_saved_path}image2index_test.json",
                # text_2_index = f"{self.config.LLM_text_embedding_saved_path}text2index_test.json",
                # config = self.config,
            )