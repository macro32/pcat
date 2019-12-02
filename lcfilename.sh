#!/bin/bash

helpFunction()
{
   echo ""
   echo "Usage: $0 -r root_dir"
   echo -e "\t-r Root dir to start depth first search"
   exit 1 # Exit script after printing help
}

while getopts "r" opt
do
   case "$opt" in
      r ) parameterA="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$parameterA" ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi

# Begin script in case all parameters are correct
echo "$parameterA"

find $1 -depth -exec rename 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \;
