#!/usr/bin/env bash

###############################################################################
## Starts a local web server hosting the app under test.
##
## Usage:
## > ./start.sh
###############################################################################

rm -rf dist/
git clone git@github.com:NBS-LLC/js-calculator.git dist/

python -m http.server --bind 127.0.0.1 -d dist/ 8080
