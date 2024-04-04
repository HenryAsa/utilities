#!/bin/zsh

# Enable extended globbing for more complex pattern matching
setopt extended_glob

# Define the regex pattern for the original filenames and the replacement string
pattern="[0-9][0-9]_some_name"
replacement="_some_new_name"

# Loop through files that match the regex pattern
for file in *(${pattern})*; do
  # Construct the new filename using the pattern and replacement
  newname="${file//$pattern/$replacement}"
  if [[ -e $newname ]]; then
    echo "File $newname already exists. Skipping $file."
  else
    # Rename the file if the new filename doesn't already exist
    mv "$file" "$newname"
    echo "Renamed $file to $newname."
  fi
done
