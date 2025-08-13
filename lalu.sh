#!/bin/bash
inpval=$1 
json=$(curl -H "Accept: application/json" "wttr.in/$inpval?format=j1" | jq .)



echo $json | jq -r '.current_condition[0] | to_entries | map("\(.key)=\(.value)") | .[]' | sed 's/\[{"value//g' | sed 's/\":"//g' | sed 's/\"}]//g'

printf "\n\n\n\n\n\n\n\n\n\n"

echo $json|jq -r .nearest_area[0]|jq -r 'to_entries | map("\(.key)=\(.value)") | .[]' | sed 's/\[{"value//g' | sed 's/\":"//g' | sed 's/\"}]//g'

printf "\n\n\n\n\n\n\n\n\n\n"

echo $json|jq -r .request[0]|jq -r 'to_entries | map("\(.key)=\(.value)") | .[]'

printf "\n\n\n\n\n\n\n\n\n\n"

echo $json|jq -r .weather[0]|jq -r 'to_entries | map("\(.key)=\(.value)") | .[]' | grep -oP '(?<=astronomy=\[).*(?=\])' | sed 's/{//g; s/}//g; s/"//g; s/,/\n/g'

printf "\n\n\n\n\n"

echo $json|jq -r .weather[0]|jq -r 'to_entries | map("\(.key)=\(.value)") | .[]' | grep -oP '(?<=hourly=\[).*(?=\])' | sed 's/{//g; s/}//g; s/"//g; s/,/\n/g' | sed 's/\[value://g' | sed 's/\]//g'

printf "\n\n\n\n\n"

echo "$json" | jq -r '.weather[0] | del(.astronomy, .hourly)' | jq -r 'to_entries | map("\(.key)=\(.value)") | .[]'

printf "\n\n\n\n\n\n\n\n\n\n"

echo $json|jq -r .weather[1]|jq -r 'to_entries | map("\(.key)=\(.value)") | .[]' | grep -oP '(?<=astronomy=\[).*(?=\])' | sed 's/{//g; s/}//g; s/"//g; s/,/\n/g'

printf "\n\n\n\n\n"

echo $json|jq -r .weather[1]|jq -r 'to_entries | map("\(.key)=\(.value)") | .[]' | grep -oP '(?<=hourly=\[).*(?=\])' | sed 's/{//g; s/}//g; s/"//g; s/,/\n/g' | sed 's/\[value://g' | sed 's/\]//g'

printf "\n\n\n\n\n"

echo "$json" | jq -r '.weather[1] | del(.astronomy, .hourly)' | jq -r 'to_entries | map("\(.key)=\(.value)") | .[]'

printf "\n\n\n\n\n\n\n\n\n\n"

echo $json|jq -r .weather[2]|jq -r 'to_entries | map("\(.key)=\(.value)") | .[]' | grep -oP '(?<=astronomy=\[).*(?=\])' | sed 's/{//g; s/}//g; s/"//g; s/,/\n/g'

printf "\n\n\n\n\n"

echo $json|jq -r .weather[2]|jq -r 'to_entries | map("\(.key)=\(.value)") | .[]' | grep -oP '(?<=hourly=\[).*(?=\])' | sed 's/{//g; s/}//g; s/"//g; s/,/\n/g' | sed 's/\[value://g' | sed 's/\]//g'

printf "\n\n\n\n\n"

echo "$json" | jq -r '.weather[2] | del(.astronomy, .hourly)' | jq -r 'to_entries | map("\(.key)=\(.value)") | .[]'