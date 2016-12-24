StackGAN
===========================================

*Edit: the authors of StackGAN released the official StackGAN [here][4]! We started this project before this release, so now there's no point in re-implementing this paper in TensorFlow.*


This is the TensorFlow implementation of the StackGAN proposed by Han Zhang et al.:

[*StackGAN: Text to Photo-realistic Image Synthesis with Stacked GANs.*][1] December 2016.

## Download data

Bird dataset: `python3 download.py cub`

or

Flower dataset: `python3 download.py cub oxford-102`

Alternatively, you can manually download the data here: [CUB][2] and [Oxford-102][3]. Once downloaded, place it on ./datasets folder.

## Work under construction!


[1]: https://arxiv.org/abs/1612.03242
[2]: https://drive.google.com/file/d/0B-y41dOfPRwROVBWUjlpM1BhbzQ/view?usp=sharing
[3]: https://drive.google.com/file/d/0B-y41dOfPRwRUzVxU3pMTEtaT1U/view?usp=sharing
[4]: https://github.com/hanzhanggit/StackGAN
