param([string]$GameDirectory = '', [string]$Suites = 'three_choice_checks,five_asset_checks,ria16_flow', [string]$Prefix = 'source', [string]$ProofFolder = 'testing/revision08')
$ErrorActionPreference = 'Stop'
$project = Split-Path -Parent $PSScriptRoot
$stage = Split-Path -Parent $project
$sdk = Join-Path $stage 'renpy-cache/sdk/8.5.3'
$proof = Join-Path $project $ProofFolder
New-Item -ItemType Directory -Path $proof -Force | Out-Null
foreach ($suite in $Suites.Split(',')) {
    $savePath = Join-Path $proof ($Prefix + '-' + $suite + '-saves')
    if ($GameDirectory) {
        $exe = Join-Path $GameDirectory 'afterwork_script_prototype.exe'
        $testArgs = @('.', 'test', $suite, '--savedir', $savePath, '--overwrite-screenshots', '--report-detailed')
        $work = $GameDirectory
    } else {
        $exe = Join-Path $sdk 'lib/py3-windows-x86_64/python.exe'
        $testArgs = @((Join-Path $sdk 'renpy.py'), $project, 'test', $suite, '--savedir', $savePath, '--overwrite-screenshots', '--report-detailed')
        $work = $project
    }
    $proc = Start-Process -FilePath $exe -ArgumentList $testArgs -WorkingDirectory $work -WindowStyle Hidden -PassThru -Wait
    $log = Join-Path $work 'log.txt'
    Copy-Item -LiteralPath $log -Destination (Join-Path $proof ($Prefix + '-' + $suite + '.log')) -Force
    Get-Content -LiteralPath $log -Tail 8
    if ($proc.ExitCode -ne 0) { exit $proc.ExitCode }
}
