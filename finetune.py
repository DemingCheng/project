import os
import torch
import platform
from colorama import Fore, Style
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
import time

def init_model():
    print("init model ...")

    model = AutoModelForCausalLM.from_pretrained(
        "gpt2",
        # torch_dtype=torch.float16,
        # device_map="cuda",
        # trust_remote_code=True
    )
 
    model.generation_config = GenerationConfig.from_pretrained(
        "gpt2"
    )

    tokenizer = AutoTokenizer.from_pretrained(
        "baichuan-inc/Baichuan-13B-Chat",
        use_fast=False,
        trust_remote_code=True
    )
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        "gpt2", 
        padding_size="left",
        # use_fast=False,
        # trust_remote_code=True
    )
    return model, tokenizer


def main(stream=True):

if __name__ == "__main__":
    main()