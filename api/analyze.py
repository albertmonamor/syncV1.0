import os


def chType(obj):
    """
        Aggressive  checking !
    """
    if os.path.isfile(obj):
        return True
    elif os.path.isdir(obj):
        return False
    else:
        try:
            open(obj).close()
            return True
        except FileNotFoundError:
            # IDK maybe need True
            return False
        except PermissionError:
            return False
        except OSError:
            return False


def fixWarpPath(text: str):
    if text.__len__() > 20:
        return f"{text[0:8]}..{text[-10:]}"

    return text


def getSubFolder(s_path, d_path):
    basename = os.path.basename(s_path)
    return d_path[d_path.find(basename) + len(basename)+1:]
