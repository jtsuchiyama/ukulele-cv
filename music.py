class Note:
    notes = ['C','C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def __init__(self, note):
        if note not in self.notes:
            raise ValueError('Invalid letter {!r}'.format(note))
        self.name = note

    def __add__(self, other):
        if isinstance(other, int):
            if other == 0:
                raise ValueError('Invalid interval number: 0')
            new_idx = (self.index() + other) % len(self.notes)
            return Note(self.notes[new_idx])
        else:
            raise ValueError('Must use an int; CHANGE ERROR LATER')

    def __str__(self):
        return self.name

    def index(self):
        return self.notes.index(self.name)

