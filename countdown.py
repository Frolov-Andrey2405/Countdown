import sys
import time
import sevseg  # Imports our sevseg.py program.

# (!) Change this to any number of seconds:
secondsLeft = 30

try:
    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)

        # Get the hours/minutes/seconds from secondsLeft:
        hours = secondsLeft // 3600
        minutes = (secondsLeft % 3600) // 60
        seconds = secondsLeft % 60

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(str(hours).zfill(2), 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(str(minutes).zfill(2), 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(str(seconds).zfill(2), 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits:
        print(f'{hTopRow}     {mTopRow}     {sTopRow}')
        print(f'{hMiddleRow}  *  {mMiddleRow}  *  {sMiddleRow}')
        print(f'{hBottomRow}  *  {mBottomRow}  *  {sBottomRow}')

        if secondsLeft == 0:
            print()
            print('    * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)  # Insert a one-second pause.
        secondsLeft -= 1
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
