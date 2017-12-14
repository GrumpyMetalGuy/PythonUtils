""" Utility functions dealing with temporary files or directories. """

import shutil
import tempfile


class TemporaryDirectoryManager(object):
    """
    Temporary directory manager context class. When initialised, will create a temporary directory. When the context
    goes out of scope, the directory and any contents will be automatically erased.
    """

    def __init__(self, delete_files=True):
        """
        Initialise temporary director manager.

        :param bool delete_files: Control whether or not to delete files when context goes out of scope.
        """
        self._temp_dir = None
        self._delete_files = delete_files

    @property
    def dir(self):
        if not self._temp_dir:
            self._temp_dir = tempfile.mkdtemp()

        return self._temp_dir

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._delete_files:
            self.clean()

    def clean(self):
        """ Clean up temporary directory, including all files contained within. """
        if self._temp_dir:
            shutil.rmtree(self._temp_dir)
            self._temp_dir = None
