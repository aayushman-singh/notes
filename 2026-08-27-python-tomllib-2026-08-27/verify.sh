#!/usr/bin/env sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
record=.verify-record
mkdir "$root/$record"
trap 'rm -rf "$record"' EXIT
sed "s#'/record/#'$record/#g" "$root/lesson.py" > "$root/$record/lesson.py"
(cd "$root" && python "$record/lesson.py")
test -f "$record/implementation.py"
