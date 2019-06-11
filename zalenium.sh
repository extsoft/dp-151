#!/usr/bin/env bash
docker run --rm -ti --name zalenium -p 4444:4444 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp/videos:/home/seluser/videos \
  -e "zalenium_no_proxy=127.0.0.1:80, 127.0.0.1:443" \
  --privileged dosel/zalenium start