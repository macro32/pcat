#!/usr/bin/bash
# usage: lcfilename <root_dir>
find $1 -depth -exec rename 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \;
