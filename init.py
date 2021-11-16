import os
import sys


def init(base_dir):
    try:
        vcs_dir = os.path.join(base_dir, '.vcs')
        obj_path = os.path.join(vcs_dir, 'objects')
        ref_path = os.path.join(vcs_dir, 'refs')
        branch_path = os.path.join(ref_path, 'branch')

        os.mkdir(vcs_dir)
        os.mkdir(obj_path)
        os.mkdir(ref_path)
        os.mkdir(branch_path)

        head_path = os.path.join(vcs_dir, 'HEAD')
        main_branch_path = os.path.join(branch_path, 'main')

        os.mknod(head_path)
        os.mknod(main_branch_path)
    except FileExistsError:
        pass


if __name__ == '__main__':
    base_dir = os.getcwd()
    try:
        base_dir = sys.argv[1]
    except IndexError:
        pass
    init(base_dir)
