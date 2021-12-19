# MrHatman26-s-Bad-Translator
A badly made program that badly uses Google Translate to translate text into random languages multiple times so that you can have some funny text.

This program uses the following modules:
  -googletrans
  -random
  -tkinter
  -threading
  -pyperclip

Updates:
1.0.0:
  -Initial Release

1.0.1:
  -Fixed a bug preventing the user from entering more text after one or more translations.
  -Prevented the user from editing the output log text box while the program is translating.

1.1.0:
  -Added an icon. (Unfortunately, the program now requires an .ico file named "Icon.ico" in the same directory or it will crash. This applies to both the python file and   the executeable)
  -Added an about button that lists very minor information about the program. (Not really much to it)
  -Prevented the user from being able to enter a number lower than or equal to one (So less than 2) as entering 1 would cause the program to never exiting the             translation loop. (And if you enter 1... Why not just use Google Translate itself? :D )
  -Added a variable that holds the current version of the program... Not particularly sure why though...
