#!/bin/bash

cat kcore.bin | strings | grep -Fx 003E0502328A -A 2  # with 003E0502328A the mac address found in get_status.cgi file