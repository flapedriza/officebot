#!/usr/bin/env sh

set -ue

python initialize_db.py

python bot.py
