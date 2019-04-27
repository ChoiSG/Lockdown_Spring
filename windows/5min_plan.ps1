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
netsh advfirewall reset
netsh advfirewall set allprofiles state on
netsh advfirewall firewall delete rule name=all
netsh advfirewall set allprofiles firewallpolicy,blockinbound,blockoutbound
netsh advfirewall firewall add rule name="Open Port 21" dir=in action=allow protocol=TCP localport=21
netsh advfirewall firewall add rule name="Open Port 21" dir=out action=allow protocol=TCP localport=21
netsh advfirewall firewall add rule name="Open Port 21" dir=in action=allow protocol=UDP localport=21
netsh advfirewall firewall add rule name="Open Port 21" dir=out action=allow protocol=UDP localport=21
netsh advfirewall firewall add rule name="Open Port 20" dir=in action=allow protocol=TCP localport=20
netsh advfirewall firewall add rule name="Open Port 20" dir=out action=allow protocol=TCP localport=20
netsh advfirewall firewall add rule name="Open Port 20" dir=in action=allow protocol=TCP localport=20
netsh advfirewall firewall add rule name="Open Port 20" dir=out action=allow protocol=TCP localport=20
#other
netstat > log.txt
