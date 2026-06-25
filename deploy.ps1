# Initialize Git Repository
git init
git add .
git commit -m "Initial commit for Life in the UK Practice App"

# Create a public GitHub repository and push
gh repo create life-in-the-uk-practice --public --source=. --remote=origin --push

# Wait a moment for GitHub to process the repo
Start-Sleep -Seconds 5

# Enable GitHub Pages using the GitHub CLI API
$repoFullName = gh repo view --json nameWithOwner -q ".nameWithOwner"
gh api -X POST /repos/$repoFullName/pages -f 'source[branch]=master' -f 'source[path]=/'

Write-Host "Deployed successfully! It may take 1-2 minutes for GitHub Pages to build."
Write-Host "You can visit your repository at: https://github.com/$repoFullName"
