import os
import sys

""" Finds the absolute path to the src folder """
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.realpath(__file__)
        )
    )
)