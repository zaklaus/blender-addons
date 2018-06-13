# ***** BEGIN GPL LICENSE BLOCK *****

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

# ***** END GPL LICENCE BLOCK *****

# constants
LOW_MSG = "At which frame does the anim state begin? "
HIGH_MSG = "At which frame does the anim state end? "

print("MD2 Animation frame names generator.")
print("Note: Ranges are denoted by open interval, ie. frame range 20-40 means 20 up to 39.")

# specify where to save the names
file_name = input("What's the file name under which we store the listing? ")

try:
    file = open(file_name, 'w')
except OSError:
    print("Error: Could not open file: " + file_name)
    exit(2)

# Get number of anim states
states = int(input("How many anim states do we want to generate? "))

# Per each state, ask for frame ranges.
old_frame = -1

for _ in range(states):
    frame_name = input("How is the anim state supposed to be called? ")
    low_frame = -1
    if old_frame != -1:
        low_frame = int(input(LOW_MSG + "[" + str(old_frame) + "] ") or str(old_frame))
    else:
        low_frame = int(input(LOW_MSG + "[0] ") or "0")

    high_frame = int(input(HIGH_MSG + "[" + str(low_frame+1) + "] ") or str(low_frame+1))
    old_frame = high_frame
    
    if low_frame >= high_frame:
        print("Error: Not a valid range!")
        exit(1)

    frame_count = high_frame - low_frame
    print("Generating frame names...")

    for j in range(frame_count):
        frame_inst = frame_name + str(low_frame + j)
        file.write(frame_inst + '\n')

file.close()
        
