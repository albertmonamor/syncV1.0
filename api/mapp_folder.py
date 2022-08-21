import os
from api.analyze import chType, getSubFolder


class MFolders(object):
    """
        class FOR Mapping Tree of Files And Folder that Into specific folder; using os.walk for recursion
            ...
            RETURN
                self.TREE = list Contains All
                    self.lisOfFiles = list Contains dict 2 value 'folder'=str, 'files'=list
                        self.li = list Contains dict 6 value [see in code]
    """

    def __init__(self):
        self.Name = os.getlogin()
        self.lisOfFiles = []
        self.li = []
        self.TREE = []
        self.SMapping_f = 0
        self.SMapping_d = 0
        self.SSyncs = None

    def __get_folder(self, Folder):
        self.li = []
        self.lisOfFiles = []
        for folder in os.walk(Folder):
            self.li = []
            self.SMapping_d += 1
            for _file in os.listdir(folder[0]):
                self.SMapping_f += 1
                fPath = fr"{folder[0]}\{_file}"
                self.li.append({"name": _file,
                                "size": os.path.getsize(fPath),
                                "time_ch": os.path.getctime(fPath),
                                "time_cr": os.path.getmtime(fPath),
                                "type": chType(fPath),
                                "sub": getSubFolder(Folder, fPath)})

            self.lisOfFiles.append({"folder": folder[0], "files": self.li})

        return self.lisOfFiles

    @staticmethod
    def __get_folder_yield(Folder):

        li = []
        lisOfFiles = []
        for folder in os.walk(Folder):
            li = []
            yield folder[0], folder[1].__len__()+folder[2].__len__()
            for _file in os.listdir(folder[0]):
                fPath = fr"{folder[0]}\{_file}"
                li.append({"name": _file,
                           "size": os.path.getsize(fPath),
                           "time_ch": os.path.getctime(fPath),
                           "time_cr": os.path.getmtime(fPath),
                           "type": chType(fPath),
                           "sub": getSubFolder(Folder, fPath)})
            lisOfFiles.append({"folder": folder[0], "files": li})

    def getFolders(self, *folders):
        """
            Folders { tuple, list }
        """

        self.TREE = []
        for folder in folders:
            self.TREE.append(self.__get_folder(folder))

        return self.TREE
