#!/bin/bash
#Script to fully clean the buildroot output
cd `dirname $0`
make -C buildroot distclean
