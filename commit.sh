#!/bin/sh
cd /Users/harukaeru/Workspace/Algorithms
git add --all
timestamp() {
  date +"at %H:%M:%S on %d/%m/%Y"
}
git commit -am "Regular auto-commit $(timestamp)"
git push origin main
