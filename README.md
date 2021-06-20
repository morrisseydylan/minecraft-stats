A Python script that inputs two JSON files and outputs one JSON file. Values from the two inputs are added together to get the value for the output. It also accounts for values that are present in one file but missing in the other.

In Minecraft, player statistics are saved as JSON files in \<world\>/stats/\<player\>.json

I created a singleplayer world using one Minecraft account but later switched to a different account. This doesn't make a difference in the world, but it resulted in two different JSON files for player statistics. I created this script to combine the files into one, so my in-game statistics would accurately reflect my total playtime. It is my first Python program.
