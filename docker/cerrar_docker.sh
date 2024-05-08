#!/bin/bash
number="${1:-}"
docker kill workshop"$number"
docker rm workshop"$number"
