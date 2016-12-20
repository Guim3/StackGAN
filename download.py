"""
Modification of https://github.com/carpedm20/DCGAN-tensorflow/blob/master/download.py
                https://github.com/stanfordnlp/treelstm/blob/master/scripts/download.py

Downloads the following:
- CUB dataset
- Oxford-102 dataset
"""

from __future__ import print_function
import os
import sys
import zipfile
import argparse
from six.moves import urllib
import tarfile

parser = argparse.ArgumentParser(description='Download dataset for StackGAN.')
parser.add_argument('datasets', metavar='D', type=str.lower, nargs='+', choices=['cub', 'oxford-102'],
                   help='name of dataset to download [CUB, Oxford-102]')
parser.add_argument('-p', '--path', metavar='dir', type=str, nargs=1,
                   help='path to store the data (default ./data)')


def download(url, dirpath):
    filename = url.split('/')[-1]
    filepath = os.path.join(dirpath, filename)
    u = urllib.request.urlopen(url)
    f = open(filepath, 'wb')
    filesize = int(u.headers["Content-Length"])
    print("Downloading: %s Bytes: %s" % (filename, filesize))

    downloaded = 0
    block_sz = 8192
    status_width = 70
    while True:
        buf = u.read(block_sz)
        if not buf:
            print('')
            break
        else:
            print('', end='\r')
        downloaded += len(buf)
        f.write(buf)
        status = (("[%-" + str(status_width + 1) + "s] %3.2f%%") %
            ('=' * int(float(downloaded) / filesize * status_width) + '>', downloaded * 100. / filesize))
        print(status, end='')
        sys.stdout.flush()
    f.close()
    return filepath


def unzip(filepath):
    print("Extracting: " + filepath)
    dirpath = os.path.dirname(filepath)
    with zipfile.ZipFile(filepath) as zf:
        zf.extractall(dirpath)
    os.remove(filepath)


def extract_tar(tar_path, extract_path='.'):
    tar = tarfile.open(tar_path, 'r')
    for item in tar:
        f_name = os.path.basename(os.path.abspath(item.name))
        if not f_name.startswith('.'):
            tar.extract(item, extract_path)
            if item.name.find('.tgz') != -1 or item.name.find('.tar') != -1:
                extract_tar(item.name, extract_path + '/' + item.name[:item.name.rfind('/')])


def download_oxford_102(dirpath):
    print('Not implemented yet!!')
    return

    data_dir = os.path.join(dirpath, 'oxford-102')
    if os.path.exists(data_dir):
        print('Found Oxford-102 - skip')
        return
    else:
        os.mkdir(data_dir)
    url = 'http://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz'
    filepath = download(url, data_dir)

    url = 'http://www.robots.ox.ac.uk/~vgg/data/flowers/102/imagelabels.mat'
    filepath = download(url, data_dir)


# Download and extracts the fila at url
def download_extract(url, data_dir):
    filepath = download(url, data_dir)
    extract_tar(filepath, data_dir)
    os.remove(filepath)


# Download CUB dataset
def download_cub(dirpath):
    data_dir = os.path.join(dirpath, 'cub')
    if os.path.exists(data_dir):
        print('Found CUB - skip')
        return
    else:
        os.mkdir(data_dir)

    # Images
    url = 'http://www.vision.caltech.edu/visipedia-data/CUB-200/images.tgz'
    download_extract(url, data_dir)

    # Labels
    url = 'http://www.vision.caltech.edu/visipedia-data/CUB-200/lists.tgz'
    download_extract(url, data_dir)

    # Annotations
    url = 'http://www.vision.caltech.edu/visipedia-data/CUB-200/attributes.tgz'
    download_extract(url, data_dir)


def prepare_data_dir(path='./data'):
    if not os.path.exists(path):
        os.mkdir(path)

if __name__ == '__main__':
    args = parser.parse_args()
    if args.path is None:
        args.path = './data'
    prepare_data_dir(args.path)

    if 'cub' in args.datasets:
        download_cub(args.path)
    if 'oxford-102' in args.datasets:
        download_oxford_102(args.path)
