import cloudmesh
from pprint import pprint

username = cloudmesh.load().username()
version = cloudmesh.version()

print username, " ", version
