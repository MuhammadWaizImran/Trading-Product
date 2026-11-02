Set-Location -LiteralPath $PSScriptRoot
Write-Host 'Open http://127.0.0.1:8765 in your browser. Press Ctrl+C to stop.'
python -m workbench.server
