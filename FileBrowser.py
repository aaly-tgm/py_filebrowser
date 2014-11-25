import os, stat, shutil

__author__ = 'aaly'


def constant(f):
    def fset(self, value):
        raise SyntaxError

    def fget(self):
        return f()

    return property(fget, fset)


class _Const(object):
    @constant
    def ABSOLUTE_PATH():
        return os.path.dirname(os.path.abspath(__file__))


class Filebrowser(object):
    """A simple example class"""

    def __init__(self):
        self.current_dir = ""


    def out(self):
        paths = self.current_dir.split("/")
        self.current_dir = ""
        for i in range(0, len(paths) - 2):
            self.current_dir += paths[i] + "/"

    def listElements(self):
        value = ""
        for root, directories, files in os.walk(self.current_dir):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                value += "<a href=\"javascript:openfile('" + filepath + "')\"><li><i class=\"icon-large icon-picture\"></i>" + filename + "</li></a>"
            for dirname in directories:
                value += "<a href=\"javascript:opendir('" + dirname + "/')\"><li><i class=\"icon-large icon-folder-open\"></i>" + dirname + "</li></a>"

        return value

    def create_dir(self, name):
        original_umask = os.umask(0)
        directory = self.current_dir + name
        if not os.path.exists(directory):
            os.mkdir(directory)
        else:
            os.chmod(directory, stat.S_IRWXO)
            os.umask(original_umask)
            return "Allready exists"

        os.chmod(directory, stat.S_IRWXO)
        os.umask(original_umask)


    def open_file(self, file):
        return '<img class="anpassen" src="' + file + '" alt="' + file + '">'


    def getCurrentDir(self):
        return self.current_dir


    def setCurrentDir(self, current_dir):
        self.current_dir = current_dir

    def move_dir(self, src_dir, dst_dir):
        shutil.move(src_dir, dst_dir)

    def rename_file(self, old_name, new_name):
        CONST = _Const()
        old_fileName = CONST.ABSOLUTE_PATH + "/" + self.current_dir + old_name
        new_fileName = CONST.ABSOLUTE_PATH + "/" + self.current_dir + new_name
        shutil.move(old_fileName, new_fileName)

    def rename_directory(self, old_name, new_name):
        CONST = _Const()
        old_dirName = CONST.ABSOLUTE_PATH + "/" + self.current_dir + old_name
        new_dirName = CONST.ABSOLUTE_PATH + "/" + self.current_dir + new_name
        shutil.move(old_dirName, new_dirName)
