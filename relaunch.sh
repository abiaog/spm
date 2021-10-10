#!/bin/bash

source kill_all_tj.sh
cp ./.taskjugglerrc.example ./.taskjugglerrc 
tj3d -c ./.taskjugglerrc -p 8474  --webserver --debug
tj3client add spm.tjp

# visit in http://127.0.0.1:8080/ or in a remote server with port 8474
