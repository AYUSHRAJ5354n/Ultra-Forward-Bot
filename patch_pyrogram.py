from typing import Union, List
import os

pyrogram_path = '/usr/local/lib/python3.8/site-packages/pyrogram/methods/users/set_profile_photo.py'

patch_content = """from typing import Union, List

class SetProfilePhoto:
    def __init__(self, emoji_background: Union[int, List[int]] = None):
        self.emoji_background = emoji_background

    def set_photo(self, photo):
        # Implement the logic to set the profile photo
        pass
"""

with open(pyrogram_path, 'w') as file:
    file.write(patch_content)

print("Patched pyrogram successfully.")
