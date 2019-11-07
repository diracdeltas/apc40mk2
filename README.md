# apc40mk2

CDJ-style looping control mapping for the APC40MKII ableton midi controller

## prerequisites

* ableton live 10.1 (may work with earlier versions but i haven't checked)
* an APC40MKII controller

## installing

1. download apc40mkii_azuki.zip
2. install it using the instructions at https://help.ableton.com/hc/en-us/articles/209072009-Installing-Third-Party-Control-Surfaces

## usage

the custom mappings are as follows:

* `METRONOME` - turns on looping for the currently selected clip (must be warped) and sets the loop start point to the nearest bar of the current playing position
* `TAP TEMPO` - sets loop end point to the nearest bar of the current playing position
* `NUDGE-` - halves the loop length
* `NUDGE+` - doubles the loop length
* `SHIFT` + NUDGE-` - moves loop position left by a bar
* `SHIFT` + NUDGE+` - moves loop position right by a bar

## credits

thanks to will marshall for doing most of the work for LooperComponent in https://github.com/willrjmarshall/AbletonDJTemplateUnsupported.

## license

http://www.wtfpl.net/
