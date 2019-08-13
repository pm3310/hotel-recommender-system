#!/usr/bin/env bash

if [ $1 = "train" ]; then
    python ./container/train
else
    python ./container/serve
fi