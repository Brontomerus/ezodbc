import hashlib
from pathlib import Path
import os
import toml
from typing import Dict

class Profile:
    
    def __init__(self, 
        connection_string: str = None, 
        profile_name: str = None
        ):
        self.profile_name: str = profile_name
        self.connection_string: str = connection_string
        file_dir_path = Path(str(Path.home())+'\\.ezodbc')
        self.file_path = Path(str(file_dir_path)+'\\profiles.toml')
        if not self._check_for_file(file_dir_path):
            self._write_initial_file()

        if self.connection_string:
            self._append_new_profile()
        


    def _check_for_file(self, path: str) -> bool:
        if not path.is_dir():
            os.mkdir(path)
        else:
            if not self.file_path.is_file():
                return False
        return True


    def _new_profile_dict(self) -> Dict:
        new_profile = {
            self.profile_name: {
                "connection": self.connection_string
            }
        }
        return new_profile


    def _write_initial_file(self) -> None:
        try:
            new_profile: Dict = self._new_profile_dict()
            with open(self.file_path, "w") as f:
                f.write('title = "ezodbc Connection Profiles"')
        except OSError as e:
            print("issue creating file in user home directory, cannot save connection profile.")

    def _append_new_profile(self) -> None:
        try:
            new_profile: Dict = self._new_profile_dict()
            with open(self.file_path, "a") as f:
                f.writelines('\n')
                toml.dump(new_profile, f)
        except OSError as e:
            print("issue creating file in user home directory, cannot save connection profile.")

    def open_profile(self) -> str:
        try:
            with open(self.file_path, "r") as f:
                profiles: Dict = toml.load(f)
            if self.profile_name in profiles:
                self.connection_string = profiles[self.profile_name]['connection']
            else:
                raise ValueError("Could not locate a profile with the given name!")
        except OSError as e:
            print("issue opening file in user home directory, cannot find given connection profile.")
        return self.connection_string

    def _encrypt_connection_string(self, connection_string: str) -> bool:
        pass
    def _decrypt_connection_string() -> str:
        pass

