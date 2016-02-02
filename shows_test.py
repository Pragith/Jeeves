from modules import shows

shows_source = 'data/shows.xml'
shows_source = "http://showrss.info/rss.php?user_id=207042&hd=0&proper=null&raw=false"


print shows.jGetShows(shows_source, 'url', 'df')
