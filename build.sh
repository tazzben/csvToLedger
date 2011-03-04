#!/bin/bash
mv src csvToLedger
tar -pczf dist/csvToLedger.tar.gz   --exclude=".*" --exclude="/.*" --exclude="/*/.*" --exclude="*.pyc" ./csvToLedger
mv csvToLedger/csvToLedger csvToLedger/csvToLedger.py
zip -r dist/csvToLedger.zip csvToLedger/[!\.]* -x \*/\.*
mv csvToLedger/csvToLedger.py csvToLedger/csvToLedger
mv csvToLedger src