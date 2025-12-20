$content = Get-Content -Path "c:\Users\mahim\OneDrive\Desktop\New folder\B2B.html" -Raw
$pattern = '(?s)<div class="slide.*?<h2 class="section-title".*?>(.*?)</h2>'
$matches = [regex]::Matches($content, $pattern)
$i = 0
foreach ($match in $matches) {
    $title = $match.Groups[1].Value.Trim()
    Write-Host "Slide $i : $title"
    $i++
}
Write-Host "Total Slides Found: $i"
