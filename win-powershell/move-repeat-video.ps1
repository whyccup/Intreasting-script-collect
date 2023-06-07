param (
    [bool]$includeSize = $false,
    [bool]$simulate = $false
)

# Define directory paths
$paths = "F:\h", "E:\h"

# Define the destination directory for duplicate files
$repeatFolder = "Path\To\Repeat\Folder"

# Check if the repeat folder exists, if not create it
if (-not (Test-Path $repeatFolder)) {
    New-Item -ItemType Directory -Path $repeatFolder | Out-Null
}

# Initialize a hashtable to store file information
$fileHashTable = @{}

# Iterate through each path
foreach ($path in $paths) {
    # Get all files in the path (excluding image files)
    $files = Get-ChildItem -Path $path -File -Recurse | Where-Object { $_.Extension -notmatch '\.(jpg|jpeg|png|gif|bmp)$' }

    # Iterate through each file
    foreach ($file in $files) {
        # Create a unique key based on the $includeSize parameter, including file name and/or size
        $fileKey = if ($includeSize) { "$($file.Length)" } else { "$($file.Name)-$($file.Length)" }

        # If the hashtable already contains the key, this means a duplicate file has been found
        if ($fileHashTable.ContainsKey($fileKey)) {
            # Move the file to the "repeat" folder and print the file name
            Write-Output "Moving file to Repeat Folder: $($file.FullName)"
            if (-not $simulate) {
                Move-Item -Path $file.FullName -Destination $repeatFolder
            }
        } else {
            # If the hashtable does not contain the key, add the key-value pair to the hashtable
            $fileHashTable[$fileKey] = $file.FullName
        }
    }
}
