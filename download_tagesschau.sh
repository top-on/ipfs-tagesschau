#!/bin/bash

wget \
    -r \
    -np \
    -k \
    -l 1 \
    -nc \
    --reject '*.jpg,*.png' \
    https://www.tagesschau.de/
