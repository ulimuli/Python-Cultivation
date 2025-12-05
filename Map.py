# 0 plains
# 1 forrest
# 2 city
# 3 high mountains
# 4 event place


class Map:
    def __init__(self):
        self.terrain = []
        self.player_pos = None
        self.impassable = {'3'}

    def load_map(self, filename="Main_Map.txt"):
        with open(filename, "r", encoding="utf-8") as f:
            lines = [ln.rstrip("\n") for ln in f.readlines()]

        self.terrain = []
        self.player_pos = None

        for r, line in enumerate(lines):
            row = []
            for c, ch in enumerate(line):
                if ch == '*':
                    # store underlying terrain as '0' by default,
                    # and record player position
                    row.append('0')
                    self.player_pos = (r, c)
                else:
                    row.append(ch)
            self.terrain.append(row)
        return self.terrain

    def get_player_terrain(self):
        """Return the terrain char (e.g. '0'..'4') under the player or None."""
        if self.player_pos is None:
            return None
        r, c = self.player_pos
        return self.terrain[r][c]

    def make_grid(self):
        """Return a copy of the terrain grid (2D list of chars)."""
        return [row[:] for row in self.terrain]

    def find_player(self):
        print(self.player_pos)
        return self.player_pos

    def can_move_to(self, r, c):
        """Return True if within bounds and not impassable."""
        if r < 0 or r >= len(self.terrain):
            return False
        if c < 0 or c >= len(self.terrain[0]):
            return False
        return self.terrain[r][c] not in self.impassable

    def move_player(self, direction):
        """
        Move the player one tile in direction.
        direction: one of 'up', 'down', 'left', 'right'
        Returns True if move succeeded, False otherwise.
        """
        if self.player_pos is None:
            raise RuntimeError("Player position unknown. Did you call load_map()?")

        dirs = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        if direction not in dirs:
            raise ValueError("direction must be 'up','down','left',or 'right'")

        r, c = self.player_pos
        dr, dc = dirs[direction]
        nr, nc = r + dr, c + dc

        if not self.can_move_to(nr, nc):
            return False

        # update player position (terrain remains unchanged)
        self.player_pos = (nr, nc)
        return True

    def display_map(self):
        """
        Return a list of strings representing the map with the player placed as '9'.
        Does NOT modify the underlying terrain.
        """
        if not self.terrain:
            return []

        out = []
        for r, row in enumerate(self.terrain):
            chars = row[:]  # copy
            if self.player_pos and self.player_pos[0] == r:
                # insert '*' at player column
                pc = self.player_pos[1]
                chars[pc] = '*'
            out.append(''.join(chars))
        return out

    def save_map(self, filename="Main_Map_out.txt"):
        """Write the displayed map (with '*') to a file."""
        with open(filename, "w", encoding="utf-8") as f:
            for line in self.display_map():
                f.write(line + "\n")


mas = Map()
mas.load_map()
mas.find_player()
print(mas.get_player_terrain())