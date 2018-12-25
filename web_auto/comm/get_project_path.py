import  os,sys
class Project_path():
    def project_path(self): 
        project_path = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0] + "/../" 
        return os.path.abspath(project_path)