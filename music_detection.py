from mingus.core.chords import determine

def chord_detection(notes):
    return determine(notes, shorthand=True)
