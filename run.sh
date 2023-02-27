#!/usr/bin/env bash

set -ue

if [ "$#" -gt 2 ]; then
  echo "Usage: $0 [--dev] [command]"
  exit 1
fi

if [ "$#" -eq 2 ]; then
  if [ "$1" = "--dev" ]; then
    docker run --rm --env-file .env -it --network host --name officebot -v "$(pwd)/data:/data" -v "$(pwd)/bot:/code" officebot "$2"
  else
    echo "Usage: $0 [--dev] [command]"
    exit 1
  fi
elif [ "$#" -eq 1 ]; then
  if [ "$1" = "--dev" ]; then
    docker run --rm --env-file .env --network host --name officebot -v "$(pwd)/data:/data" -v "$(pwd)/bot:/code" officebot
  else
    docker run -it --env-file .env --rm --name officebot -v "$(pwd)/data:/data" officebot "$1"
  fi
else
  docker run --rm -d --env-file .env --name officebot -v "$(pwd)/data:/data" officebot
fi
