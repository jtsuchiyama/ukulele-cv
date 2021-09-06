# Ukulele Chord Recognition

This repository is an adaptation of Paulden's Guitar Fingering Recognition work. I do not claim ownership for any of his work. Personal changes properly detect the location of fingers and chord building using mingus. 

## How to run

- `rotate_crop_tests.py`: doing its best to rotate the neck as horizontally as possible and cropping image around the neck
- `grid_detection_tests.py`: working hard on the construction of the grid of notes (i.e. the separation between strings and between frets)
- `finger_detection_tests.py`: concentrating its energy on the detection of fingertips on the neck (but currently failing)
- `full_test.py`: runs all features to locate the strings, frets, notes, and chords

Time performance will be displayed as well as original images and result images.

Should you have a look at how the code is running, open `rotate_crop.py`, `grid_detection.py` and `finger_detection.py`.

## Credits

https://github.com/paulden/guitar-fingering-recognition


