tell application "Finder"
	set project_path to (container of container of (path to me)) as string
end tell
set posix_project_path to POSIX path of project_path
do shell script "python " & posix_project_path & "capture.py"
display notification "Screencapture link is copied to clipboard!" with title "Screencapture"
