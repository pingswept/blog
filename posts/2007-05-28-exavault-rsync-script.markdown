---
date: 2007-05-28T00:00:00.000Z
format: markdown
title: Exavault rsync script
---

The company I work for recently started using a service called <a href="http://exavault.com">Exavault</a> to back up our data. We have a server running Linux that logs into our NAS using ssh every night and rsyncs the data with a local directory. It also dumps our mediawiki database (well, used to-- we're using <a href="http://socialtext.net/open">Socialtext</a> now) and subversion repository.

All of this data gets synchronized with Exavault's machines in Dublin, California.

This has been running with no known problems for about six months. Below are the bash scripts I wrote to do the synchronization.

$$code(lang=bash)
LOGFILE=/var/log/GME_backup/GME_backups.log
echo "Syncing chemp to Exavault, starting $(date +%FT%T)" >> $LOGFILE
echo "Dumping wiki database" >> $LOGFILE
mv /home/brandon/wiki_backup/wiki_dump /home/brandon/wiki_backup/wiki_dump.old
mysqldump --user=root --password=****** greenmountain > /home/brandon/wiki_backup/wiki_dump
rm /home/brandon/wiki_backup/wiki_dump.old
echo "Dumped wiki database" >> $LOGFILE
echo "Dumping Subversion repository" >> $LOGFILE
mv /home/brandon/svn_backup/svn_dump /home/brandon/svn_backup/svn_dump.old
svnadmin dump /home/brandon/svn/NCL2 > /home/brandon/svn_backup/svn_dump
rm -r /home/brandon/svn_backup/svn_dump.old
echo "Dumped Subversion repository" >> $LOGFILE
echo "Backing up files from Q, SVN, and wiki" >> $LOGFILE
rsync -av --exclude-from=no_backup.txt --progress /home/brandon/Q_backup/ greenmountain@greenmountain.exavault.com:backup-test/ >> $LOGFILE
rsync -av --exclude-from=no_backup.txt --progress /home/brandon/svn_backup/ greenmountain@greenmountain.exavault.com:backup-svn/ >> $LOGFILE
rsync -av --exclude-from=no_backup.txt --progress /home/brandon/wiki_backup/ greenmountain@greenmountain.exavault.com:backup-wikidb/ >> $LOGFILE
rsync -av --exclude-from=no_backup.txt --progress /var/www/wiki/ greenmountain@greenmountain.exavault.com:backup-wiki/ >> $LOGFILE
echo "Finished at $(date +%FT%T)" >> $LOGFILE
echo "----------------***-------------------" >> $LOGFILE</pre>
$$/code

The other script:

$$code(lang=bash)
#!/bin/bash
LOGFILE=/var/log/GME_backup/GME_backups.log
echo "Syncing Q to Chemp, starting $(date +%FT%T)" >> $LOGFILE
rsync -a --exclude-from=no_backup.txt --progress root@192.168.2.4:/raid/WeatherPhenom/  /home/brandon/Q_backup/ >> $LOGFILE
echo "Finished at $(date +%FT%T)" >> $LOGFILE
echo "---------------------------------" >> $LOGFILE</pre>
$$/code
