"""module docstring"""
from time import sleep

from loguru import logger
from tqdm import tqdm

for i in tqdm(range(10), desc="Outer Loop", unit="epoch"):
    # for j in tqdm(range(100), desc="Inner Loop", unit="batch"):
    sleep(0.1)
    logger.info("some info message")
    logger.critical("some critical message")
