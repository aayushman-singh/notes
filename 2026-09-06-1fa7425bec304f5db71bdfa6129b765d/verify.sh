#!/usr/bin/env sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
docker run --rm --network=none --read-only --cap-drop=ALL --security-opt=no-new-privileges --memory=1g --cpus=1.0 --pids-limit=128 --tmpfs=/record:rw,noexec,nosuid,size=16m --mount "type=bind,src=$root,dst=/artifact,readonly" python:3.11-slim@sha256:1042b61448fef4ba92d16a8c7eb4996d027568ce64792a7877fd88511e0af7c6 python /artifact/source_experiment.py
