# Start this program at the beginning of a homework break.
# It will then run for $1 minutes (and make that particular
# terminal shell inoperable) and then calls caramelldansen as
# an alarm.

# Where the music lives
MUSIC_DIRECTORY=/home/jonah/Storage/Music

# The song you want to play
SONG=Caramell_-_Caramelldansen_\(Speedycake_Remix\).mp3

# The music player program 
PLAYER=mplayer

# Tells us that the program is running
echo "Alright, take your break."
echo "I'll tell you when you're done."

# Waits the required amount of time
sleep $@ # 2 = 2 seconds, 1 m = 1 minute, 2 h = 2 hours

# Calls an obnoxious song using mplayer and
# forces you to shut it off and get back to work
$PLAYER $MUSIC_DIRECTORY/$SONG
