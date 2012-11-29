from django.conf.urls.defaults import *

#=============================================================================== Patterns
urlpatterns = patterns('buzzer.views',
                       url(r'^trebek[/]?', 'trebek'),
                       url(r'^board[/]?', 'board'), 
                       (r'', 'player'),
		       )
