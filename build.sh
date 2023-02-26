#!/usr/bin/env bash

set -ue

DEV=''

if [ "$#" -gt 1 ]; then
  echo "Usage: $0 [--dev]"
  exit 1
fi

if [ "$#" -eq 1 ]; then
  if [ "$1" = "--dev" ]; then
    DEV='true'
  else
    echo "Usage: $0 [--dev]"
    exit 1
  fi
fi

docker build -f docker/Dockerfile -t "officebot" --build-arg DEV="$DEV" .
