import enum



class CommentType(str, enum.Enum):
    episode = "Episode"
    character = "Character"
    characterInEpisode="CharacterInEpisode"

class StatusType(str, enum.Enum):
    new = "New"
    review = "Review"
    Rejected="Rejected"
    approved="Approved"
