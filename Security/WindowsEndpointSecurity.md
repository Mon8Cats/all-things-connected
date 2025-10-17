# Windows Endpoints

```cmd
tasklist /v /fi "session eq 1"
tasklist /m /fi "session eq 14" /fo csv >>c:\users\mxo4300\desktop\session-14-modules.csv

wmic process list full | more   // deprecated?
```

LOLBins: Living Off the Land Binaries