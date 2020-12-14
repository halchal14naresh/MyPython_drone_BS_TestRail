from selenium_base.path import GetPath
from utilities.generic_functions import GenericFunctions


class MoveToArchiveFolder:
    paths = GetPath()

    def move_to_archive(self, archive_dir_path, source_dir):
        """
        Moving old files to archive folder. This is specially for execution reports
        """
        dir_name = GenericFunctions.get_filename_datetimestamp()


        print("dir_name  " , dir_name)


        if 'windows' in GenericFunctions.get_os().casefold():
            GenericFunctions.isdir_present(archive_dir_path + "\\", dir_name)
            GenericFunctions.move_directories(source_dir, archive_dir_path + "\\" + dir_name)
        else:
            # code for linux or mac
            pass
