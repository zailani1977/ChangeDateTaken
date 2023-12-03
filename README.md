# ChangeDateTaken.py

## Author
Zailani

## Version
1.0.0

## Description
This Python script updates the date taken of an image file. It will alter the DateTimeOriginal, DateTime, and DateTimeDigitized tags.

## Dependencies
- [exif]: A Python library to extract and edit EXIF data from JPEG images.

## Usage
To run the script, you need to provide two arguments:
- `directory`: The directory containing JPG files that you want to change the date taken.
- `shift_value`: The shift value in the format "days:hours:minutes" that you want to add or subtract from the original date taken.

For example, if you want to shift the date taken of all JPG files in the folder "Photos" by 2 days, 3 hours, and 15 minutes, you can run the following command:

```bash
python ChangeDateTaken.py Photos 2:3:15
```

The script will print the original and shifted dates for each file that it updates.

## License
This script is free and open source. You can use it for any purpose, but I am not responsible for any damages or losses that may occur from using it. Use it at your own risk.
