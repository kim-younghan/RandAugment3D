import torch
import torchvision.transforms as transforms
from RandAugment3D.augmentations import RandAugment3D
from cv2 import cv2


def preprocessing(point_set, cls):
    pts_transform = transforms.Compose(
        []
    )
    pts_transform.transforms.insert(0, RandAugment3D(2, 2))
    
    return torch.from_numpy(pts_transform(point_set)), cls