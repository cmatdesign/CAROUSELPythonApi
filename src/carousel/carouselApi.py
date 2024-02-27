import ctypes

# Carousel API
class Carousel:
    def __init__(self, LibraryPath=None):
        self.dll = ctypes.WinDLL(LibraryPath)
        self.api = self.get_api_object()
        self.luaCommand = self.get_api_command_handle()

    def __str__(self):
        return f"Carousel api:{self.LibraryPath}"
    
    def get_api_object(self):
        get_API_controll_default = self.dll.get_API_controll_default
        get_API_controll_default.restype = ctypes.POINTER(ctypes.c_int)
        api = get_API_controll_default()
        return api
    
    def get_api_command_handle(self):
        API_run_lua_command = self.dll.API_run_lua_command
        API_run_lua_command.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_char_p]
        API_run_lua_command.restype = ctypes.c_char_p
        return API_run_lua_command
    
    def run_command(self, command, properties=b''):
        result = self.luaCommand(self.api, command, properties)
        return ctypes.cast(result, ctypes.c_char_p).value.decode("utf-8")

# Static class that maps carousel api methods
class CarouselApis:
    
    @staticmethod
    def project_load_id(carousel, projectId):
       return carousel.run_command(b'project_loadID_L',str(projectId).encode('utf-8'))
   
    @staticmethod
    def project_loadName(carousel, projectName):
       return carousel.run_command(b'project_loadName',str(projectName).encode('utf-8'))
   
    # =================================================================================================================
    #                                           CONFIGURATIONS
    # =================================================================================================================
    @staticmethod
    def configuration_get_working_directory(carousel):
        return carousel.run_command(b'configuration_get_working_directory')
    
    @staticmethod
    def configuration_set_working_directory(carousel, workingDirectory):
        return carousel.run_command(b'configuration_set_working_directory', str(workingDirectory).encode('utf-8'))        
    
    @staticmethod
    def configuration_get_thermodynamic_database_path(carousel):
        return carousel.run_command(b'configuration_get_thermodynamic_database_path')
    
    @staticmethod
    def configuration_set_thermodynamic_database_path(carousel, databasePath):
        return carousel.run_command(b'configuration_set_thermodynamic_database_path', str(databasePath).encode('utf-8'))        
    
    @staticmethod
    def configuration_get_physical_database_path(carousel):
        return carousel.run_command(b'configuration_get_physical_database_path')
    
    @staticmethod
    def configuration_set_physical_database_path(carousel, databasePath):
        return carousel.run_command(b'configuration_set_physical_database_path', str(databasePath).encode('utf-8'))    
    
    @staticmethod
    def configuration_get_mobility_database_path(carousel):
        return carousel.run_command(b'configuration_get_mobility_database_path')
    
    @staticmethod
    def configuration_set_mobility_database_path(carousel, databasePath):
        return carousel.run_command(b'configuration_set_mobility_database_path', str(databasePath).encode('utf-8'))   
    
    @staticmethod
    def configuration_get_max_thread_number(carousel):
        return carousel.run_command(b'configuration_get_max_thread_number')
    
    @staticmethod
    def configuration_set_max_thread_number(carousel, maxThreads):
        return carousel.run_command(b'configuration_set_max_thread_number', str(maxThreads).encode('utf-8'))   

    @staticmethod
    def configuration_save(carousel):
        return carousel.run_command(b'configuration_save')  
    
    # =================================================================================================================
    #                                           CONFIGURATIONS
    # =================================================================================================================
