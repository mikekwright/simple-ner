import os
import logging
import json

import numpy as np

logger = logging.getLogger(__name__)


class IrisReader:
    def __init__(self, data_filename, seed=42):
        self._data_filename = data_filename
        self._seed = seed
        self._random = np.random.RandomState(seed=seed)

    def __call__(self, split=0.2):
        with open(self._data_filename, 'r') as iris_file:
            iris_data = json.load(iris_file)

        self._random.shuffle(iris_data)
        split_index = int(len(iris_data) * split)

        return iris_data[:split_index], iris_data[split_index:]

    def store_results(self, directory):
        os.makedirs(directory, exist_ok=True)

        data_config = {
            'seed': self._seed,
            'data_filename': self._data_filename,
        }
        with open(os.path.join(directory, 'config.json'), 'w', encoding='utf-8') as config_file:
            json.dump(data_config, config_file, indent=4, ensure_ascii=False)
