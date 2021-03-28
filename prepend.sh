# modified from https://gist.github.com/thebearjew/79f5f572baa8dc8e6d492a282c7d4fc9
# Given a file path as an argument
# 1. get the file name
# 2. prepend template string to the top of the source file
# 3. resave original source file

filepath="$1" 
file_name=$(basename $filepath | awk -F'[-]' '{print $2}' | awk -F'[.]' '{print $1}' | sed 's/\(.\)\([A-Z]\)/\1 \2/g') 

# Getting the file name (title)
md='.md'
title=${file_name%$md}
title2=$title 

# Prepend front-matter to files
TEMPLATE="---
sidebar_label: $title2 
title: ' '
---

"

echo "$TEMPLATE" | cat - "$filepath" > temp && mv temp "$filepath"

#  find ./docs/ -name "*.md" -print0 | xargs -0 -I file ./prepend.sh file