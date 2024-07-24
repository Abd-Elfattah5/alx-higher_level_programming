#!/bin/bash
# obtaining the available methods to the responses
curl -sI $1 | grep -i Allow | awk -F': ' '{print $2}'
