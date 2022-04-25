import enum



class CommentType(str, enum.Enum):
    episode = "Episode"
    character = "Character"
    characterInEpisode="CharacterInEpisode"

