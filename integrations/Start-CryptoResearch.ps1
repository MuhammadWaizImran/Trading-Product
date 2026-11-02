param(
    [ValidateSet('offline', 'check', 'research')][string]$Mode = 'offline',
    [string]$Symbol = 'BTC-USD',
    [string]$Model = 'openai/gpt-oss-20b'
)
$ErrorActionPreference = 'Stop'
$pythonPath = Join-Path $PSScriptRoot '.venv-tradingagents/Scripts/python.exe'
$runnerPath = Join-Path $PSScriptRoot 'run_crypto_research.py'
if (-not (Test-Path -LiteralPath $pythonPath)) { throw 'Install the isolated environment first; see TRADINGAGENTS_SETUP.md.' }
$previousKey = $env:GROQ_API_KEY
$secretPointer = [IntPtr]::Zero
try {
    if ($Mode -ne 'offline') {
        $secureKey = Read-Host 'Enter your replacement Groq key (hidden; never paste it in chat)' -AsSecureString
        $secretPointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureKey)
        $env:GROQ_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($secretPointer)
    }
    & $pythonPath $runnerPath --mode $Mode --symbol $Symbol --model $Model
    if ($LASTEXITCODE -ne 0) { throw 'Research launcher did not complete successfully.' }
} finally {
    $env:GROQ_API_KEY = $previousKey
    if ($secretPointer -ne [IntPtr]::Zero) { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($secretPointer) }
    if ($secureKey) { $secureKey.Dispose() }
}
