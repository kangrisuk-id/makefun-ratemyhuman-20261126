#!/usr/bin/env python3
"""Rate My Human: The One-Line Review"""

REVIEWS = [
    "Solid 7/10 — occasionally forgets where they left their keys, but tries hard.",
    "5 stars for effort, minus 2 for leaving the fridge open overnight.",
    "Adequate human. Would recommend for light emotional support and snack sharing.",
    "3.5/10: good at breathing, needs improvement on punctuality.",
    "10/10 would exist again — solid contribution to the carbon cycle.",
]

import random

if __name__ == "__main__":
    print(random.choice(REVIEWS))
