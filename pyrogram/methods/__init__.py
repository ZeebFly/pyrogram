
from .advanced import Advanced
from .auth import Auth
from .bots import Bots
from .chats import Chats
from .contacts import Contacts
from .decorators import Decorators
from .invite_links import InviteLinks
from .messages import Messages
from .password import Password
from .premium import Premium
from .users import Users
from .stories import Stories
from .utilities import Utilities


class Methods(
    Advanced,
    Auth,
    Bots,
    Contacts,
    Password,
    Premium,
    Chats,
    Users,
    Stories,
    Messages,
    Decorators,
    Utilities,
    InviteLinks,
):
    pass
