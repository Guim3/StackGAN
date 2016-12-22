import os  # for reading files and directories
import numpy as np  # for arrays

"""DatasetReader: reads dataset images and texts into numpy arrays.
Also, an optional normalization can be applied over all the data."""


class DatasetReader:

    def __init__(self, dataset, path=None, normalize=True):
        """ __dataset = (str) dataset type: ['cub',  'oxford-102']
            __path = (str) path to the dataset. If not specified, it will look to './datasets/{cub | oxford-102}'
            __normalization = (bool) if True, normalizes all the images of the dataset to be [-1, 1]."""

        # Check that dataset type is valid
        dataset = dataset.lower()
        assert dataset == 'cub' or dataset == 'oxford-102', \
            "Dataset not recognized: %s. Must be 'cub' or 'oxford-102'" % dataset

        self.__dataset = dataset

        # Initialize path, if not specified
        if path is None:
            self.__path =  os.path.abspath(__file__ + "/../../") + '/datasets/' + self.__dataset

        # Check if path exists
        assert os.path.exists(self.__path), "Path %s does not exist" % self.__path

        self.__normalize = normalize

    def method(self):
        """Input:
                - blabla:
           Output:
                - blabla: """
        pass

if __name__ == '__main__':
    pass