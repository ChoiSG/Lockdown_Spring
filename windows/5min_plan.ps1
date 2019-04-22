# Change Password
$admin = (Read-Host -Prompt "New Admin Password" -AsSecureString)
Set-ADAccountPassword -Identity Administrator -NewPassword $admin -Reset
#creat local admin
$Password = (Read-Host -Prompt "New local Admin Password" -AsSecureString)
New-LocalUser "Admin1" -Password $Password 
Add-LocalGroupMember -Group "Administrators" -Member "Admin1"
#disbale scheduled tasks
Clear-DnsClientCache
Clear-ARPCache
Stop-Service DFSR
Get-ScheduledTask | Disable-ScheduledTask
#firewall
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
netsh advfirewall reset
netsh advfirewall firewall add rule  protocol=TCP dir=in localport = 342 action=block
New-NetFirewallRule -Direction Inbound -Action allow -LocalPort 80 -Protocol TCP
New-NetFirewallRule -Direction Ouybound -Action allow -LocalPort 80 -Protocol TCP
New-NetFirewallRule -Direction Inbound -Action Block -LocalPort 22 -Protocol TCP
New-NetFirewallRule -Direction Outbound -Action Block -LocalPort 22 -Protocol TCP
#other
netstat > log.txt