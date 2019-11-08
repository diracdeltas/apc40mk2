from _Framework.ButtonElement import ButtonElement


def quantize(num):
    return round(num / 2.0) * 2.0


def button_assert(button):
    assert ((button is None) or (isinstance(button, ButtonElement) and button.is_momentary()))


class LooperComponent():
  'Handles looping controls'
  __module__ = __name__

  def __init__(self, parent):
    self._parent = parent
    self._loop_on_button = None
    self._loop_end_button = None
    self._loop_stop_button = None
    self._loop_halve_button = None
    self._clip_length = 0
    self._current_clip = None
    self._track_number = 0

  def set_track_number(self, number):
    self._track_number = number

  def get_loop_length(self):
    if self._current_clip is not None:
        clip = self._current_clip
        return clip.loop_end - clip.loop_start
    else:
        return 0

  def set_loop_on_button(self, button):
    button_assert(button)
    if self._loop_on_button != button:
      if self._loop_on_button is not None:
        self._loop_on_button.remove_value_listener(self.start_loop)
      self._loop_on_button = button
      if (self._loop_on_button is not None):
        self._loop_on_button.add_value_listener(self.start_loop)

  def start_loop(self, value):
    # toggles loop, sets start point to the current playing position
    if value > 0:
      self.get_current_clip()
      if self._current_clip is not None:
        current_clip = self._current_clip
        if self._clip_length == 0:
          self._clip_length = current_clip.length
        current_position = current_clip.playing_position
        current_clip.looping = 1
        # set end to the end of the song for now
        current_clip.loop_end = quantize(self._clip_length)
        # set start to the current position
        current_clip.loop_start = quantize(current_position)

  def set_loop_end_button(self, button):
    button_assert(button)
    if self._loop_end_button != button:
      if self._loop_end_button is not None:
        self._loop_end_button.remove_value_listener(self.end_loop)
      self._loop_end_button = button
      if (self._loop_end_button is not None):
        self._loop_end_button.add_value_listener(self.end_loop)

  def end_loop(self, value):
    # sets end point to the current playing position
    if value > 0:
      self.get_current_clip()
      if self._current_clip is not None:
        current_clip = self._current_clip
        if current_clip.looping:
          current_position = current_clip.playing_position
          current_clip.loop_end = quantize(current_position)

  def set_loop_stop_button(self, button):
    button_assert(button)
    if self._loop_stop_button != button:
      if self._loop_stop_button is not None:
        self._loop_stop_button.remove_value_listener(self.stop_loop)
      self._loop_stop_button = button
      if (self._loop_stop_button is not None):
        self._loop_stop_button.add_value_listener(self.stop_loop)

  def stop_loop(self, value):
    if value > 0:
      self.get_current_clip()
      if self._current_clip is not None:
        self._current_clip.looping = 0

  def set_loop_halve_button(self, button):
    button_assert(button)
    if self._loop_halve_button != button:
      if self._loop_halve_button is not None:
        self._loop_halve_button.remove_value_listener(self.decrease_loop)
      self._loop_halve_button = button
      if (self._loop_halve_button is not None):
        self._loop_halve_button.add_value_listener(self.decrease_loop)

  def decrease_loop(self, value):
    if value > 0:
      self.get_current_clip()
      if self._current_clip is not None:
        current_clip = self._current_clip
        if current_clip.looping:
          loop_length = self.get_loop_length()
          current_clip.loop_end = current_clip.loop_start + loop_length / 2.0

  def get_current_clip(self):
    song = self._parent.song()
    # log = self._parent.log_message()
    clip_slots = song.tracks[self._track_number].clip_slots
    if (clip_slots is None):
        self._current_clip = None
        return
    for clip_slot in clip_slots:
        if clip_slot.has_clip and clip_slot.is_playing:
            self._current_clip = clip_slot.clip
            return
        else:
            self._current_clip = None
