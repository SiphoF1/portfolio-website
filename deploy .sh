#!/bin/bash

# Navigate to the directory containing the HTML file
cd ~/Desktop/PLP\ Course/HTML

# Check if the file exists
if [ -f "portfolio website.html" ]; then
    echo "HTML file found. Proceeding..."
else
    echo "Error: HTML file 'portfolio website.html' not found."
    exit 1
fi

# Initialize Git repository
git init

# Add the HTML file to the staging area
git add "portfolio website.html"

# Commit the changes
git commit -m "Add portfolio website HTML file"

# Add your GitHub repository as a remote (replace with your GitHub URL)
git remote add origin https://github.com/SiphoF1/HTML-PLP-2024.git

# Push your changes to GitHub
git push -u origin master

# Check if push was successful
if [ $? -eq 0 ]; then
    echo "Code successfully pushed to GitHub."
else
    echo "Error: Failed to push code to GitHub."
fi
