# apc40mk2

CDJ-style looping control mapping for the APC40MKII ableton midi controller

## prerequisites

* ableton live 10.1 (may work with earlier versions but i haven't checked)
* an APC40MKII controller

## installing

1. download release.zip from https://github.com/diracdeltas/apc40mk2/releases/latest
2. unzip it
3. copy the unzipped `apc40mkii_azuki` folder to your Ableton MIDI remote
   scripts directory using the instructions at
   https://help.ableton.com/hc/en-us/articles/209072009-Installing-Third-Party-Control-Surfaces.
   for instance on Mac with Ableton 10, this would be `/Applications/Ableton
   Live 10 Suite.app/Contents/App-Resources/MIDI Remote Scripts`.
4. open Ableton Preferences with your apc40mk2 plugged in and select `apc40mkii
   azuki` as the control surface.

## usage

the custom mappings are as follows:

* `METRONOME` - turns on looping for the currently selected clip (must be warped) and sets the loop start point to the nearest bar of the current playing position
* `TAP TEMPO` - sets loop end point to the nearest bar of the current playing position
* `NUDGE-` - moves loop position left by a bar
* `NUDGE+` - moves loop position right by a bar
* `SHIFT NUDGE-` - halves the loop length
* `SHIFT NUDGE+` - doubles the loop length. currently this is somewhat buggy
  and will cause the play position to jump sometimes (i think this
  is an ableton bug)

## credits

thanks to will marshall for doing most of the work for LooperComponent in https://github.com/willrjmarshall/AbletonDJTemplateUnsupported.

## license

http://www.wtfpl.net/
