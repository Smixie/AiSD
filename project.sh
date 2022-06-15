#!/bin/bash
 
if [ $# -lt 1 ]
then
         echo "Unexpected syntax"
         echo "usage: $0 <site>"
         exit
 fi
 
 Help()
 {
    # Display Help
    echo "Add description of the script functions here."
    echo
    echo "Syntax: scriptTemplate [-g|h|s|t]"
    echo "options:"
    echo "g     Get some info"
    echo "h     Print this Help."
    echo "s     Url to find"
    echo "t     Time between next check"
    echo
 }
 Info()
 {
    echo "Czekanie na zmiany"
    echo "Projekt na Systemy operacyjne"
    echo "2022"
 }
 
 Main()
 {
         i=1
         for value in "${arr[@]}"
         do
                 curl $value > "$i""_sites_last"
                 i=$((i+1))
         done
         echo "Now please wait!"
 
         while true
         do
	         sleep $1
                 j=1
                 for value in "${arr[@]}"
                 do
                         curl "$value" > "$j""_sites_now"
                         if [[ $(diff "$j""_sites_last" "$j""_sites_now") ]]
                         then
                                 firefox "$value"
                                 cp "$j""_sites_now" "$j""_sites_last"
                                 echo "Changes has been made on $j, site was open"
                         else
                                 echo "No changes"
                         fi
                         j=$((j+1))
                 done
         done
 }

 while getopts ":ght:s:" option; do
    case $option in
       g) #info
          Info
          exit;;
       h) # display Help
          Help
          exit;;
       t) # Enter time
          time=$OPTARG;;
       s) arr+=($OPTARG);;
      \?) # Invalid option
          echo "Error: Invalid option"
          exit;;
    esac
 done
 
 Main $time $arr
