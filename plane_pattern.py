from plane_builder import SpiralBuilder, TableBuilder

class PlanePattern:
  # pylint: disable=no-self-argument
  def is_odd(n):
    return n % 2 == 1

  def __init__(self, descriptor = "mod_2", condition = is_odd):
    self.condition = condition
    self.descriptor = descriptor

  def file_descriptor(self):
    raise NotImplementedError

  def from_data(self, sequence_data):
    raise NotImplementedError

class SpiralPattern(PlanePattern):
  def file_descriptor(self):
    if self.descriptor == "":
      return "_spiral"
    else:
      return f"_spiral_{self.descriptor}"

  def from_data(self, sequence_data):
    return SpiralBuilder(sequence_data, self.condition).grid

class TablePattern(PlanePattern):
  def file_descriptor(self):
    if self.descriptor == "":
      return "_tabl"
    else:
      return f"_tabl_{self.descriptor}"

  def from_data(self, sequence_data):
    return TableBuilder(sequence_data, self.condition).grid
