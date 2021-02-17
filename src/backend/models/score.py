

class ScoreRecord:
    def __init__(self, row=None):
        self.Username = ''
        self.Score = 0
        self.GameId = ''
        self.Id = ''
        if None != row:
            self.Username = row.get('username', '')
            self.Score = row.get('score', 0)
            self.GameId = row('game_id', '')
            self.Id = row('id', '')
    def as_dict(self):
        return {
            'username' : self.Username,
            'score' : self.Score,
            'game_id': self.GameId,
            '_id' : self.Id,
        }