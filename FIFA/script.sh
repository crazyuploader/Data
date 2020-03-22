#!/usr/bin/env bash

echo ""
echo "Getting Player IDs"
python Get_Player_ID.py
echo "Done!"
echo ""
echo "Getting Player Info"
python Get_Player_Info.py
echo "Done!"
echo ""
cat Players_Info.csv
echo ""
echo "Script Finished"
