#!/bin/bash
# obtaining the length of the response body
curl -sI $1 | grep -i content-length | awk '{print $2}'
