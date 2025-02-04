from model import *
import pytest

def test_str_encode():
    print('testing str_encode')
    emb = PatchEmbedder()
    test_str = "test"
    print(emb.encode_patch(test_str))
    test_sentence = "this is a test sentence!"
    print(emb.encode_patch(test_sentence))
    
def test_patcherize_str():
    print('testing patcherize_str')
    emb = PatchEmbedder()
    test_sentence = "this is a test sentence!"
    patches = emb.patcherize_str(x=test_sentence, p_size=4)
    print([emb.encode_patch(p) for p in patches])
    
    
    
    
if __name__ == '__main__':
    test_str_encode()
    test_patcherize_str()
