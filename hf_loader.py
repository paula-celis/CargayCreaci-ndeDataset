
from datasets import load_dataset


class HFDatasetLoader:
    def __init__(self, dataset_name, split="train", config=None):
        self.dataset_name = dataset_name
        self.split = split
        self.config = config

    def load(self):
        dataset = load_dataset(
            self.dataset_name,
            name=self.config,
            split=self.split
        )

        dataframe = dataset.to_pandas()
        return dataframe
