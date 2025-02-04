from model import *
import pytest

def test_str_encode():
    emb = PatchEmbedder()
    test_str = "test"
    print(emb.str_encode(test_str))
    test_sentence = "this is a test sentence!"
    print(emb.str_encode(test_sentence))
    
    
    
if __name__ == '__main__':
    test_str_encode()
