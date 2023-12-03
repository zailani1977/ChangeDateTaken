"""
Script Name: ChangeDateTaken.py
Author: Zailani
Version: 1.0.0
Description: 
    This Python script updates the date taken of an image file. It will alters the
    DateTimeOriginal, DateTime, and DateTimeDigitized tags.
Dependencies:
    exif
"""
import exif
import argparse
from datetime import datetime, timedelta
import os

def changeExifDate(directory, shift_value):
    # Iterate over all the JPG files in the directory
    for filename in os.listdir(directory):
        filename = filename.lower()
        if filename.endswith(".jpg"):
            # Create the full file path
            image_file = os.path.join(directory, filename)

            # Open the image file and read the exif data
            with open(image_file, 'rb') as image:
                exif_data = exif.Image(image)

            # Get the DateTimeOriginal value as a datetime object
            original_date = datetime.strptime(exif_data.get('datetime_original'), "%Y:%m:%d %H:%M:%S")

            # Calculate the shifted date by adding or subtracting the shift value
            shift_days, shift_hours, shift_minutes = map(int, shift_value.split(':'))
            shifted_date = original_date + timedelta(days=shift_days, hours=shift_hours, minutes=shift_minutes)

            # Convert the shifted date to a string
            shifted_date_str = shifted_date.strftime("%Y:%m:%d %H:%M:%S")

            # Set the DateTimeOriginal, DateTime, and DateTimeDigitized values to the shifted date
            exif_data.set('datetime_original', shifted_date_str)
            exif_data.set('datetime', shifted_date_str)
            exif_data.set('datetime_digitized', shifted_date_str)

            # Write the modified exif data back to the image file
            with open(image_file, 'wb') as image:
                image.write(exif_data.get_file())

            # Print the original and shifted dates
            print(f'Updated file: {filename}')
            print(f'\tOriginal date: {original_date}')
            print(f'\tShifted date: {shifted_date}')
            

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='Directory containing JPG files')
    parser.add_argument('shift_value', help='Shift value in format "days:hours:minutes"')
    args = parser.parse_args()

    # Call the sub function to change the exif date for each JPG file in the directory
    changeExifDate(args.directory, args.shift_value)