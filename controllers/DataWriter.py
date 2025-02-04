class DataWriter():    
    def write_export_files(self,data,filename):
        raise _NotImplementError("children must implement this method")
    
class RowExcelData:
    
    def __init__(self,data):
        self._data = data

    @property
    def header(self):
        return  list(self._data and self._data[0].keys())
    
    @property
    def rows(self):
        return [list(row.values()) for row in self._data]
    
class DataManger:
    
    def __init__(self, writer : DataWriter):
        self.writer = writer
        
    def save(self,data,filename):
        return self.writer.write_export_files(data,filename)
    
class Error(DataWriter):
    
    def read(self,filename):
        return "success"

class _NotImplementError(Exception):
    pass
