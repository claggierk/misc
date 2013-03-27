REM Change the "Year" variable below to whatever year you want to be created...
set YEAR=2003
set TRUE=T

REM Make the YEAR directory
mkdir %YEAR%

REM Make the month directories within the YEAR directory
FOR %%M IN (01 02 03 04 05 06 07 08 09 10 11 12) DO mkdir %YEAR%\%%M

REM Make the day directories within each month's directory (all months have at least 28 days every year...)
FOR %%M IN (01 02 03 04 05 06 07 08 09 10 11 12) DO FOR %%D IN (01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28) DO mkdir %YEAR%\%%M\%%D

REM Apr, Jun, Sep, Nov all have 30 days...
FOR %%M IN (04 06 09 11) DO FOR %%D IN (29 30) DO mkdir %YEAR%\%%M\%%D

REM Jan, Mar, May, Jul, Aug, Oct, Dec all have 31 days...
FOR %%M IN (01 03 05 07 08 10 12) DO FOR %%D IN (29 30 31) DO mkdir %YEAR%\%%M\%%D

REM Feb has 29 days on leap years... need to determine if YEAR is a leap year...
SET isLeapYear=F

::Check if the year is evenly divisible by 400
SET /a _modYear=%YEAR% / 400
SET /a _modYear=%_modYear% * 400
If %_modYear%==%YEAR% SET isLeapYear=T
If %_modYear%==%YEAR% GOTO LEAP_YEAR_DETERMINED

::Check if the year is evenly divisible by 100
SET /a _modYear=%YEAR% / 100
SET /a _modYear=%_modYear% * 100
If %_modYear%==%YEAR% SET isLeapYear=F
If %_modYear%==%YEAR% GOTO LEAP_YEAR_DETERMINED

::Check if the year is evenly divisible by 4
SET /a _modYear=%YEAR% / 4
SET /a _modYear=%_modYear% * 4
If %_modYear%==%YEAR% SET isLeapYear=T
If %_modYear%==%YEAR% GOTO LEAP_YEAR_DETERMINED

:LEAP_YEAR_DETERMINED
echo %isLeapYear%

If %isLeapYear%==%TRUE% mkdir %YEAR%\02\29
