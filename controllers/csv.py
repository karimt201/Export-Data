import csv
import controllers.DataWriter as DW
import Serializer as sr
import http
import exceptions
import data_handler as dh

class CSVCreator(DW.DataWriter):

    def __init__(self,test_csv_writer=None):
        self.test_csv_writer  = test_csv_writer  or csv

    def write_export_files(self,data,filename):
        
        with open(filename, 'w',newline='') as csv_file:
            wr = self.test_csv_writer.writer(csv_file)
            wr.writerow(data.header)
            wr.writerows(data.rows)
            
        return filename

class CsvController:
  
  def create_csv(self):
    try:
      candidate = dh.database_handle().get_all()
      Serializer = sr._DataSerializer(candidate)._data_serialize()
      row_data = DW.RowExcelData(Serializer)
      csv_file = CSVCreator()
      manger = DW.DataManger(csv_file)
      self.create_csv_manger(manger,row_data,"Export_All_candidate.csv")
      return self.create_csv_Serializer(candidate,"Export_All_candidate.csv")
    except exceptions._NotFoundError as exc:
      return sr._DataSerializer()._core_error_serialize(exc,http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND  
    
  
  # def create_csv_paginated(self):
  #   try:
  #     candidate = dh.database_handle().get_paginated(page=1,per_page=3)
  #     Serializer = sr._DataSerializer(candidate)._data_serialize()
  #     row_data = DW.RowExcelData(Serializer)
  #     csv_file = CSVCreator()
  #     manger = DW.DataManger(csv_file)
  #     self.create_csv_manger(manger,row_data,"Export_candidate_paginated.csv") 
  #     return self.create_csv_Serializer(candidate,"Export_All_candidate.csv")
  #   except exceptions._NotFoundError as exc:
  #     return sr._DataSerializer()._core_error_serialize(exc,http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND  
    
  def create_csv_record(self,candidate_id):
    try:
      candidate = dh.database_handle().get(candidate_id)
      Serializer = sr._DataSerializer(candidate)._data_serialize()
      row_data = DW.RowExcelData([Serializer])
      csv_file = CSVCreator()
      manger = DW.DataManger(csv_file)
      self.create_csv_manger(manger,row_data,"Export_One_candidate.csv") 
      return self.create_csv_Serializer(candidate,"Export_All_candidate.csv")
    except exceptions._NotFoundError as exc:
      return sr._DataSerializer()._core_error_serialize(exc,http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND  

  def create_csv_manger(self,manger,row_data,filename):
    return manger.save(row_data,filename)
  
  def create_csv_Serializer(self,candidate,filename):
    return sr._DataSerializer(candidate,filename)._All_serialize(),http.HTTPStatus.OK
  