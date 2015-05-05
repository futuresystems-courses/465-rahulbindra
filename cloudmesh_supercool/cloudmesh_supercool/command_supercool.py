import os
from cloudmesh_base.Shell import Shell


class command_supercool(object):

    @classmethod
    def status(cls,file):
	
	root_path = "/home/ubuntu"
	return os.path.isfile(os.path.join(root_path,file))
        
