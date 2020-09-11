#!/bin/bash
(
  # make sure we're in the right dir since we rm -rf..
  cd $(dirname "$0")

  (
    mkdir tmp
    cd tmp
    wget https://github.com/tailwindlabs/heroicons/archive/master.zip
    unzip master.zip
  )

  rm -rf heroicons/static/heroicons
  mv tmp/heroicons-master/optimized heroicons/static/heroicons
  rm -rf tmp
)
