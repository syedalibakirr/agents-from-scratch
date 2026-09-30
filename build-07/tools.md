# Tools

## list_files
List all file paths in the repo.

## read_file
Read one file, 150 lines at a time, with line numbers. Pass a repo-relative path, and optionally start_line to read further down.

## search
Searches the repo for a given string and returns the matching lines.

## edit_file
Change a file by replacing one exact piece of text with new text. old_text must appear exactly once in the file. To create a new file, pass an empty old_text and the full file contents as new_text.
