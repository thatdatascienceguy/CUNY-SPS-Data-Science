#!/bin/bash
SQF_ZIP=$(ls *.zip)
for i in $SQF_ZIP; do
	unzip $i
done
