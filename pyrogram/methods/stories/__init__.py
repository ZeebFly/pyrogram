
from .can_send_story import CanSendStory
from .copy_story import CopyStory
from .delete_stories import DeleteStories
from .edit_story import EditStory
from .export_story_link import ExportStoryLink
from .forward_story import ForwardStory
from .get_all_stories import GetAllStories
from .get_peer_stories import GetPeerStories
from .get_pinned_stories import GetPinnedStories
from .get_stories import GetStories
from .get_stories_archive import GetStoriesArchive
from .hide_stories import HideStories
from .increment_story_views import IncrementStoryViews
from .pin_stories import PinStories
from .read_stories import ReadStories
from .send_story import SendStory

class Stories(
    CanSendStory,
    CopyStory,
    DeleteStories,
    EditStory,
    ExportStoryLink,
    ForwardStory,
    GetAllStories,
    GetPeerStories,
    GetPinnedStories,
    GetStories,
    GetStoriesArchive,
    HideStories,
    IncrementStoryViews,
    PinStories,
    ReadStories,
    SendStory,
):
    pass
