"""enums."""
import enum


class CommentType(str, enum.Enum):
    """Comment's type."""
    episode = "Episode"
    character = "Character"
    characterInEpisode="CharacterInEpisode"

class StatusType(str, enum.Enum):
    """Comment's status"""
    new = "New"
    review = "Review"
    Rejected="Rejected"
    approved="Approved"
