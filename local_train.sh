#!/usr/bin/env bash

docker run -v ${PWD}/local_test:/opt/ml --rm hotel-recommender-system train