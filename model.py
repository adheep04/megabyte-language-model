import torch
import torch.nn as nn
import torch.nn.functional as F

v_size = 256
d_model = 1024
p_size = 16


#TODO
class MegabyteLanguageModel(nn.Module):
    def __init__(self,):
        self.patch_embed = PatchEmbedder()
        self.global_ = GlobalModel()
        self.local = LocalModel()
        return
    
    def forward(self, x):
       return 

#TODO
class PatchEmbedder(nn.Module):
    def __init__(self, v_size, d_model, p_size):
        self.embed = nn.Embedding(v_size, d_model)
        return
    
    def forward(self, x):
        '''
        args:
        - x: [str]
            - len(x) = emb_len * patch_size
        output
        - tensor(b, emb_len, patch_size, d_emb)
        
        '''
        return 
    
    @staticmethod
    def patch_encode(patch: str, p_size: int) -> torch.Tensor:
        return [ord(char.encode('utf-8')) for char in x]
    
    def chunk_str(x: str, p_size: int):
        
            
#TODO
class GlobalModel(nn.Module):
    def __init__(self,):
        return
    
    def forward(self, x):
       return 

#TODO
class LocalModel(nn.Module):
    def __init__(self,):
        return
    
    def forward(self, x):
       return 
