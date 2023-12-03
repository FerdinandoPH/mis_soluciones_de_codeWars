function Get-PhoneNumberValidation([String]$PhoneNumber)
{
  # TODO code solution
  
  if($PhoneNumber.Length -ne 14){
    
  	Return $false
  }

  if ($PhoneNumber[0] -ne "(" -or $PhoneNumber[4] -ne ")" -or $PhoneNumber[5] -ne " " -or $PhoneNumber[9] -ne "-"){
    
  	Return $false
  }
  $shouldBeNumbers=@(1,2,3,6,7,8,10,11,12,13)
  foreach ($i in $shouldBeNumbers){
  	if ([Char]::IsDigit($PhoneNumber[$i]) -eq $false){
    	Return $false
    }
  }
  Return $true
}
Get-PhoneNumberValidation "(123) 456-7890"