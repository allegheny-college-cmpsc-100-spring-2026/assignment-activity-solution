import os
import sys

""" Finds the absolute path to the src folder """
activity_src = os.path.dirname(
    os.path.dirname(
        os.path.realpath(__file__)
    )
)
sys.path.append(
    activity_src
)
sys.path.append(
    f"{activity_src}/src"
)