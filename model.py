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
        self.global_ = Decoder()
        self.local = Decoder()
        return
    
    def forward(self, x):
       return 

#TODO
class PatchEmbedder(nn.Module):
    def __init__(self, 
        v_size: int = v_size, 
        d_model: int = d_model, 
        p_size: int = p_size
        ):
        super().__init__()
        
        self.p_size = p_size
        self.embed = nn.Embedding(v_size, d_model)
        print(self.embed)
        return
    
    def forward(self, x: str):
        patches = [self.encode_patch(p) for p in 
                   self.patcherize_str(x=x, p_size=self.p_size)]
        
        return 
    
    def embed_patch(patch: list[int]) -> torch.Tensor:
        
    
    @staticmethod
    def encode_patch(patch: str) -> torch.Tensor:
        '''
        'this'
        -> 
        [116, 104, 105, 115]
        '''
        return [ord(char.encode('utf-8')) for char in patch]
    
    @staticmethod
    def patcherize_str(x: str, p_size: int):
        '''
        'this is a sentence!'
        -> 
        ['this', ' is ', 'a te', 'st s', 'ente', 'nce!']
        '''
        return [x[i:i+p_size] for i in range(0, len(x), p_size)]
        
            
# class Decoder(nn.Module):

