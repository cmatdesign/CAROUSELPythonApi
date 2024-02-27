from carousel import carouselDatabase

class Project:
    def __init__(self, ID=None, Name=None, API_Name=None, External_APIName=None):
        self.ID = ID
        self.Name = Name
        self.API_Name = API_Name
        self.External_APIName = External_APIName
        self.Cases = []

    def __str__(self):
        return f"ID: {self.ID}, Name: {self.Name}, API_Name: {self.API_Name}, External_APIName: {self.External_APIName}"

    def load_scheil_simulation_data(self, db_handler):
        for case in self.Cases:
            case.load_simulations_from_database(db_handler)

    @staticmethod
    def load_cases(db_handler, project_id):
        return Case.get_all_cases_for_project(db_handler, project_id)
        
    @staticmethod
    def load(db_handler, project_id):
        #Load Project data
        loaded = db_handler.load_from_query_first_or_default(Project, f'SELECT * FROM Projects WHERE ID=' + str(project_id))
        
        #Load Additional data
        loaded.Cases = Project.load_cases(db_handler, project_id)
        return loaded

class Case:
    def __init__(self, ID=-1, IDProject=-1, IDGroup=-1, Name="", Script="", Date="", PosX=0, PosY=0, PosZ=0, SheilSimulations=None):
        self.ID = ID
        self.IDProject = IDProject
        self.IDGroup = IDGroup
        self.Name = Name
        self.Script = Script
        self.Date = Date
        self.PosX = PosX
        self.PosY = PosY
        self.PosZ = PosZ
        self.SheilSimulations = SheilSimulations if SheilSimulations is not None else []

    def __str__(self):
        return f"ID: {self.ID}, IDProject: {self.IDProject}, IDGroup: {self.IDGroup}, Name: {self.Name}, Script: {self.Script}, Date: {self.Date}, PosX: {self.PosX}, PosY: {self.PosY}, PosZ: {self.PosZ}"

    # Loads scheil simulation data
    def load_simulations_from_database(self, db_handler):
        simulation_items = db_handler.load_from_query(ScheilSimulation, f'SELECT * FROM vd_ScheilSimulation WHERE IDCase=' + str(self.ID))
        self.SheilSimulations = simulation_items
    
    # Method returns all cases for a given project ID
    @staticmethod
    def get_all_cases_for_project(db_handler, projectID):
        case_items = db_handler.load_from_query(Case, f'SELECT * FROM `Case` WHERE IDProject=' + str(projectID))
        return case_items

class ScheilSimulation:
    def __init__(self, Temperature=700, PhaseFraction=0, PhaseName="", ProjectName="", IDCase=-1, IDPhase=-1, IDProject=-1):
        self.Temperature = Temperature
        self.PhaseFraction = PhaseFraction
        self.PhaseName = PhaseName
        self.ProjectName = ProjectName
        self.IDCase = IDCase
        self.IDPhase = IDPhase
        self.IDProject = IDProject

    def __str__(self):
        return f"Temperature: {self.Temperature}, PhaseFraction: {self.PhaseFraction}, PhaseName: {self.PhaseName}, ProjectName: {self.ProjectName}, IDCase: {self.IDCase}, IDPhase: {self.IDPhase}, IDProject: {self.IDProject}"
