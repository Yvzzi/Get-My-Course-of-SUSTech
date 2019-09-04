Param(
	[parameter(Mandatory=$false)][String[]] $python = "python",
	[parameter(Mandatory=$false)][String[]] $pip = "pip"
)

$msg = Read-Host "Had you installed Chrome? [y/N]"
if ($msg.ToLower().Trim() -eq 'n') {
    echo "Please install Chrome before you run the script."
    echo "https://www.google.cn/intl/zh-CN/chrome/"
    exit 0
}

$tmpPath = $path + "\tmp"

if (!$env:path.Contains("Python") -and !$env:path.Contains("python")) {
	curl -Uri "https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe" -OutFile "python-install.exe"
	./python-install.exe
	del python-install.exe
}
$str = Invoke-Expression "& $pip list"
if (-not "$str".Contains("selenium")) {
    & $pip install -i $pipUrl selenium
}
if (-not "$str".Contains("requests")) {
    & $pip install -i $pipUrl requests
}
echo "Please download the driver manually and move it to directory Scripts where you install Python"
echo "http://npm.taobao.org/mirrors/chromedriver"
