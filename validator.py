import re
import exceptions

class _DataValidator():  
  def __init__(self,json_body=None):
    self.json_body= json_body
    
  def _All_validate(self):
    if isinstance(self.json_body,list):
      for body in self.json_body:
        self.validate(body)
    else:
      self.validate(self.json_body)
      
  def validate(self,body):
    self.is_valid_name(body.get('name'))
    self.is_valid_email(body.get('email'))
    self.is_valid_compatibility(body.get('compatibility'))
    self.is_valid_sourcing(body.get('sourcing'))
    self.is_valid_status(body.get('status'))
  
  def is_valid_name(self,name):
    if not name: raise exceptions._RequiredInputError('Name is required')
    self._is_valid_name(name)
  
  def _is_valid_name(self,name):
    if not isinstance(name, str): raise exceptions._InvalidInputError('Name is not valid string')
    
  def is_valid_email(self,email):
    if not email: raise exceptions._RequiredInputError('Email is required')
    self._is_valid_email(email)
    
  def _is_valid_email(self,email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+",email): raise exceptions._InvalidInputError('Email is not valid')
  
  def is_valid_compatibility(self,compatibility):
    if compatibility is not None:
      if not compatibility: raise exceptions._RequiredInputError('Compatibility is required')
      self._is_valid_compatibility(compatibility)
    else:
      return compatibility
    
  def _is_valid_compatibility(self,compatibility):
    if not isinstance(compatibility, (int)): raise exceptions._InvalidInputError('Compatibility must be a number')
  
  def is_valid_sourcing(self,sourcing):
    if not sourcing: raise exceptions._RequiredInputError('Sourcing is required')
    self._is_valid_sourcing(sourcing)
    
  def _is_valid_sourcing(self,sourcing):
    if not isinstance(sourcing,str): raise exceptions._InvalidInputError('Sourcing is not valid string')
    
  def is_valid_status(self,status):
    if not status: raise exceptions._RequiredInputError('Status is required')
    self._is_valid_status(status)
    
  def _is_valid_status(self,status):
    if not isinstance(status,str): raise exceptions._InvalidInputError('Status is not valid string')
