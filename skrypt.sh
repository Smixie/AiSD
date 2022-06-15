#!/bin/bash

if [ $# -lt 1 ]
then
	echo "Unexpected syntax"
	echo "usage: $0 <site>"
	exit
fi

for sites in "$@";
do
	arr+=($sites)
done

i=1
for value in "${arr[@]}"
do
	curl $value > "$i""_sites_last"
	i=$((i+1))
done
echo "Now please wait!"

while true
do
	sleep 10
	j=1
	for value in "${arr[@]}"
	do
		curl "$value" > "$j""_sites_now"
		if [[ $(diff "$j""_sites_last" "$j""_sites_now") ]]
		then
			firefox "$value"
			cp "$j""_sites_now" "$j""_sites_last"
		else
			echo "No changes"
		fi
		j=$((j+1))
	done
done
