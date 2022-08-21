from api.mapp_folder import MFolders
import os
from shutil import copy2


class SyncFolders(MFolders):
    """
        work with class MFolder
    """

    def __init__(self):
        super(SyncFolders, self).__init__()
        self.liFilesMain = []
        self.slash = "\\"

    def sync(self, folder: list[list, list], RSL: bool = True):
        """
            RSL => Index OF -R_oot- folder in List Of parameter `folder`;
                   Index OF -S_ub Folder- [..];
                   Index OF -(for) L_oop- [..]
        """
        if RSL:
            indexR = 0
            indexS = 1
            indexL = 1

        else:
            indexR = 1
            indexS = 0
            indexL = 0

        Root = folder[indexR]
        FolderTS = folder[indexS][0]['folder'].replace("/", "\\")
        for __ in folder[indexL]:

            for _ in Root:

                for create in _['files']:

                    c_s = create['sub']
                    Path = rf"{FolderTS}\{c_s}"
                    if not create['type']:
                        if not os.path.exists(Path):
                            os.mkdir(Path)

                    else:
                        if os.path.exists(Path) and create['type']:
                            if not create['size'] == os.path.getsize(Path):
                                print(Path)
                                os.system(rf"del {Path}")

                        if not os.path.exists(Path):
                            copy2(f"{_['folder']}\\{create['name']}", f"{FolderTS}\\{c_s[:c_s.rfind(self.slash)+1]}")