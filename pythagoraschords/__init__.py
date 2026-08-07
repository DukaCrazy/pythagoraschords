class PythagorasChords:
# Pythagoras v0.0.1
# Implements the fundamental structure of triads: root, third, and fifth.
# The next version (0.0.2) will expand the system to include seventh and ninth intervals.
# In a future release, Pythagoras will also compute real frequency values for each note.

    notes_all_sharp = ["A", "A♯", "B", "C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯"]
    notes_all_bemol = ["A", "B♭", "B", "C", "D♭", "D", "E♭", "E", "F", "G♭", "G", "A♭"]
    triad = [
        [0, 4, 7],
        [2, 5, 9],
        [4, 7, 11],
        [5, 9, 0],
        [7, 11, 0],
        [9, 0, 4],
        [11, 2, 5]
    ]

    def __init__(self, tone: str):
        self.tone = tone.upper()
        self.number = self._init_number(self.tone)

    def _init_number(self, tone: str) -> int:
        match tone:
            case "A": return 0
            case "A#" | "A♯" | "AS" | "BB" | "B♭": return 1
            case "B": return 2
            case "C": return 3
            case "C#" | "C♯" | "CS" | "DB" | "D♭": return 4
            case "D": return 5
            case "D#" | "D♯" | "DS" | "EB" | "E♭": return 6
            case "E": return 7
            case "F": return 8
            case "F#" | "F♯" | "FS" | "GB" | "G♭": return 9
            case "G": return 10
            case "G#" | "G♯" | "GS" | "AB" | "A♭": return 11
        return 0

    def _triad_method(self, number: int, sharp_flat = False):
        result = []

        for tonic, third, fifth in self.triad:
            t = (tonic + number) % 12
            th = (third + number) % 12
            f = (fifth + number) % 12

            if sharp_flat == True:
                result.append([self.notes_all_bemol[t], self.notes_all_bemol[th], self.notes_all_bemol[f]])
            elif sharp_flat == False:
                result.append([self.notes_all_sharp[t], self.notes_all_sharp[th], self.notes_all_sharp[f]])

        return result

    def get_number(self):
        return self.number

    def get_tone(self):
        return self.tone

    def get_triad_array(self, sharp_flat = False):
        return self._triad_method(self.number, sharp_flat)