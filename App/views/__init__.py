# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .game import game_views
from .index import index_views
from .auth import auth_views
from .usergame import user_game_views


views = [user_game_views,user_views, index_views,game_views, auth_views] 
# blueprints must be added to this list