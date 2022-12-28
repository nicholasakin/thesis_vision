#!/bin/bash

#renames .jpg images to img_#.jpg

COUNTER=0
for IMG in $(ls *.jpg)
do
	#preserve name removes .jpg
	#NAME=$(echo "$IMG" | sed -e "s/.jpg//")

	echo $(mv $IMG "img_${COUNTER}.jpg")
	mv $IMG "img_${COUNTER}.jpg"
	let COUNTER++
done
	





