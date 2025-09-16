# Windows and AD Fundamentals - Summary

Learned about Windows file systems and services: NTFS, FAT, HPFS, and ADS (Alternate Data Streams in NTFS). Also noted WMI (Windows Management Instrumentation) and VSS (Volume Shadow Copy Service).  
Reviewed basic `cmd` commands: `hostname`, `whoami`, `ipconfig`, `netstat`, and `net`. Useful helpers include `command /?` for manuals and `cls` to clear the screen.  
Looked at Windows advanced options such as opening Windows Update via `control /name Microsoft.WindowsUpdate` and firewall profiles (domain, private, public) managed through `WF.msc`.  
Studied Active Directory concepts: Domain Controllers, AD DS, users as security principals, Group Policy Objects (GPOs), and SYSVOL for policy distribution. GPOs apply settings to OUs and configure either computers or users.  
Learned about Windows authentication protocols: Kerberos (modern) and NetNTLM (legacy). Kerberos works with tickets, using the Key Distribution Center (KDC) on the Domain Controller to issue TGTs (Ticket Granting Tickets) and TGS (Ticket Granting Service) tickets. NetNTLM uses a challenge-response system.  
Also covered AD structure: domains can form trees (e.g. `uk.thm.local` and `us.thm.local`) and forests (different namespaces, e.g. `THM` and `MTH`). Enterprise Admins have authority over the entire forest.  