#!/bin/sh
cd /Users/harukaeru/Workspace/Algorithms
git add --all
timestamp() {
  date +"%Y/%m/%d %H:%M:%S"
}
git commit -am "$(timestamp)"
git push origin main
