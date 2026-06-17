from dataclasses import make_dataclass
from functools import lru_cache
from dacite import from_dict

# The goal of this is to convert nested dictionaries into dynamically generated nested dataclasses

# Option 1
# Step 1. Generate dataclass tree with all values. Also generate possible dataclasses
# Step 2. Populate that tree using dacite

# Option 2
# Step 1. Generate tree and populate it at the same time


class DacitifyDataset:
    def __init__(self, dataset):
        self.dataset = dataset
        pass

    def generate(self):
        # self.dataclass = make_dataclass('Node', fields=[('s', str)])
        pass

    @lru_cache(maxsize=5)
    def populate(self, dataclass, dataset: dict):
        pass
        fields = {}
        for k, v in dataset.items():
            if type(v) is dict:
                self.populate(dataclass, v)
            else:
                pass
