#!/bin/bash

# Create directories for categories if they do not exist
mkdir -p Movies Pictures Music

# Move files to corresponding directories
for file in *; do
    if [[ -f $file ]]; then
        case "${file##*.}" in
            mp3|aac)
                mv "$file" Music/
                ;;
            mov|mp4)
                mv "$file" Movies/
                ;;
            png|jpg)
                mv "$file" Pictures/
                ;;
        esac
    fi
done

echo "Files have been sorted into Movies, Pictures, and Music directories."