import shutil
import os
from kolyabin_yuriy_dz_seven_two import create_a_project


def assembly_templates(name_project):
    """Функция собирает все шаблоны в одну папку templates"""
    root_proj = os.path.join('./', name_project)
    dst_dir = os.path.join(root_proj, 'templates')
    os.makedirs(dst_dir, exist_ok=True)
    for root, dirs, files in os.walk(root_proj):
        if root.count('templates'):
            for _ in dirs:
                os.makedirs(os.path.join(dst_dir, _), exist_ok=True)
            for file in files:
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_dir, os.path.basename(root))
                if not os.path.dirname(src_file) == dst_file:
                    shutil.copy(src_file, dst_file)


create_a_project()

if __name__ == '__main__':
    assembly_templates('my_project')
