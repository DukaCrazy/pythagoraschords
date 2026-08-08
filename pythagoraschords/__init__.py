class PythagorasChords:

    def __init__(self, tone: str):
        self.tone = tone.upper()
        self.number = self._init_number(self.tone)
        self._init_all_list()

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

    def _init_all_list(self):
        """
        T - 2th - 3th - 4th - 5th - 6th - 7th
        0 -  2  -  4  -  5  -  7  -  9  -  11
        T  - 3th - 5th - 7th - 9th - 11th- 13th
        0  -  4  -  7  -  11 -  2  -  5  -  9
        """
        self.notes_all_sharp = ["A", "A♯", "B", "C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯"]
        self.notes_all_bemol = ["A", "B♭", "B", "C", "D♭", "D", "E♭", "E", "F", "G♭", "G", "A♭"]
        self._major_diatonic_list = [ 
            [0, 4, 7, 11, 2, 5, 9],
            [2, 5, 9, 0, 4, 7, 11],
            [4, 7, 11, 2, 5, 9, 0],
            [5, 9, 0, 4, 7, 11, 2],
            [7, 11, 2, 5, 9, 0, 4],
            [9, 0, 4, 7, 11, 2, 5],
            [11, 2, 5, 9, 0, 4, 7]
        ]

        self._major_scale_list = [
            [0, 2, 4, 5, 7, 9, 11],
            [2, 4, 5, 7, 9, 11, 2],
            [4, 5, 7, 9, 11, 0, 2],
            [5, 6, 9, 11, 0, 2, 4],
            [7, 9, 11, 0, 2, 4, 5],
            [9, 11, 0, 2, 4, 5, 7],
            [11, 0, 2, 4, 5, 7, 9]
        ]

    def _get_diatonic_sequence(self, number: int, sequence_type = 0, sharp_flat = False):

        if sequence_type == 0:
            major_list = self._major_scale_list
        else:
            major_list = self._major_diatonic_list
        result = []

        for tonic, note_2, note_3, note_4, note_5, note_6, note_7 in major_list:
            iTonik = (tonic + number) % 12
            inote_2 = (note_2 + number) % 12
            inote_3 = (note_3 + number) % 12
            inote_4 = (note_4 + number) % 12
            inote_5 = (note_5 + number) % 12
            inote_6 = (note_6 + number) % 12
            inote_7 = (note_7 + number) % 12

            if sharp_flat == True:
                result.append([self.notes_all_bemol[iTonik], self.notes_all_bemol[inote_2], self.notes_all_bemol[inote_3], self.notes_all_bemol[inote_4], self.notes_all_bemol[inote_5], self.notes_all_bemol[inote_6], self.notes_all_bemol[inote_7]])
            elif sharp_flat == False:
                result.append([self.notes_all_sharp[iTonik], self.notes_all_sharp[inote_2], self.notes_all_sharp[inote_3], self.notes_all_sharp[inote_4], self.notes_all_sharp[inote_5], self.notes_all_sharp[inote_6], self.notes_all_sharp[inote_7]])

        return result

    #0
    def get_number(self):
        return self.number

    #A
    def get_tone(self):
        return self.tone

    #['A', 'B', 'C♯', 'D', 'E', 'F♯', 'G♯']
    def get_major_scale(self, sharp_flat = False):
        return self._get_diatonic_sequence(self.number, 0, sharp_flat)[0]
    
    #[['A', 'C♯', 'E'], ['B', 'D', 'F♯'], ['C♯', 'E', 'G♯'], ['D', 'F♯', 'A'], ['E', 'G♯', 'B'], ['F♯', 'A', 'C♯'], ['G♯', 'B', 'D']]
    def get_major_triad_scale(self, sharp_flat = False):
        result = []
        for triad in self._get_diatonic_sequence(self.number, 1, sharp_flat):
            result.append([triad[0],triad[1],triad[2]])
        return result

    #['A', 'C♯', 'E']
    def get_triad(self, triad = 0, sharp_flat = False):
        triad_list = self._get_diatonic_sequence(self.number, 1, sharp_flat)[triad]
        return [triad_list[0],triad_list[1],triad_list[2]]

    #[['A', 'C♯', 'E', 'G♯', 'B', 'D', 'F♯'], ['B', 'D', 'F♯', 'A', 'C♯', 'E', 'G♯'], ['C♯', 'E', 'G♯', 'B', 'D', 'F♯', 'A'], ['D', 'F♯', 'A', 'C♯', 'E', 'G♯', 'B'], ['E', 'G♯', 'B', 'D', 'F♯', 'A', 'C♯'], ['F♯', 'A', 'C♯', 'E', 'G♯', 'B', 'D'], ['G♯', 'B', 'D', 'F♯', 'A', 'C♯', 'E']]
    def get_diatonic_extended_chords(self, sharp_flat = False):        
        return self._get_diatonic_sequence(self.number, 1, sharp_flat)

    #['A', 'C♯', 'E', 'G♯', 'B', 'D', 'F♯']
    def get_diatonic_extended_chord(self, sub_scale = 0, sharp_flat = False):        
        return self._get_diatonic_sequence(self.number, 1, sharp_flat)[sub_scale]

    #A
    def get_diatonic_extended_degree(self, sub_scale = 0, note = 0, sharp_flat = False):        
        return self._get_diatonic_sequence(self.number, 1, sharp_flat)[sub_scale][note]
