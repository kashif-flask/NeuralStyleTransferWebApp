import torch
import torch.optim as optim
import torch.nn as nn
from PIL import Image
import torchvision.transforms as transforms
import torchvision.models as models
from torchvision.utils import save_image

class VGG(nn.Module):
    def __init__(self):
        super(VGG,self).__init__()
        self.choosen_features=['0','5','10','19','28']
        self.model=models.vgg19(pretrained=True).features[:29]
    def forward(self,x):
        features=[]
        for layer_num,layer in enumerate(self.model):
            x=layer(x)
            if str(layer_num) in self.choosen_features:
                features.append(x)
        return features

device=torch.device("cuda" if torch.cuda.is_available() else "cpu")


model=VGG().to(device).eval()



