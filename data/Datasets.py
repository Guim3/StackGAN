import numpy as np

"""Dataset: given dataset images and their labels, constructs a dataset and generates mini-batches. """
class Dataset:
    def __init__(self, images, labels):
        """ Input:
            - images: numpy array N x height x width x color, where N is the number of samples
            - labels: numpy array NxM, where M is the dimensionality of the labels.
        """

        self._num_examples = len(labels)
        self._index_in_epoch = 0
        self._epochs_completed = 0

        perm = np.arange(self._num_examples)
        np.random.shuffle(perm)

        self._images = images[perm]

        self._labels = labels[perm]

    def set_data(self, images, labels):
        self._images = images
        self._labels = labels

    def get_images(self):
        return self._images

    def get_labels(self):
        return self._labels

    def next_batch(self, batch_size):
        """Return the next `batch_size` examples from this data set."""
        start = self._index_in_epoch
        self._index_in_epoch += batch_size
        if self._index_in_epoch > self._num_examples:
            # Finished epoch
            self._epochs_completed += 1
            # Shuffle the data
            perm = np.arange(self._num_examples)
            np.random.shuffle(perm)
            self._images = self._images[perm]
            self._labels = self._labels[perm]
            # Start next epoch
            start = 0
            self._index_in_epoch = batch_size
            assert batch_size <= self._num_examples
        end = self._index_in_epoch
        return self._images[start:end], self._labels[start:end]
