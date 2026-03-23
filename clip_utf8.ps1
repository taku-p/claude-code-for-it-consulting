# clip_utf8.ps1 - UTF-8対応クリップボードコピー
# Usage: powershell -ExecutionPolicy Bypass -File clip_utf8.ps1 -File "path/to/file.txt"
# Usage: powershell -ExecutionPolicy Bypass -File clip_utf8.ps1 -Text "テキスト"

param(
    [string]$File,
    [string]$Text
)

if ($File) {
    $content = [System.IO.File]::ReadAllText($File, [System.Text.Encoding]::UTF8)
    Set-Clipboard -Value $content
    Write-Host "Copied to clipboard from: $File"
} elseif ($Text) {
    Set-Clipboard -Value $Text
    Write-Host "Copied to clipboard."
} else {
    # Read from stdin
    $input_text = @()
    while ($line = [Console]::In.ReadLine()) {
        $input_text += $line
    }
    $joined = $input_text -join "`n"
    Set-Clipboard -Value $joined
    Write-Host "Copied to clipboard from stdin."
}
