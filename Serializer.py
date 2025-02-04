class _DataSerializer():
  def __init__(self,user=None,filename=None):
    self.user =  user
    self.filename=filename
    
  def _data_serialize(self):
    if isinstance(self.user, list):
      return [self.serialize(user) for user in self.user]
    return self.serialize(self.user)
    
  def _All_serialize(self):
    if isinstance(self.user, list):
      return [self.all_serialize(user) for user in self.user]
    return self.all_serialize(self.user)
    
  def _request_serialize(self):
    if isinstance(self.user, list):
      return [self.request_serialize(user) for user in self.user]
    return self.request_serialize(self.user)
    
  def serialize(self,user=None):
    user = user or self.user
    return {
            'name': user.name,
            'email': user.email,
            'compatibility':user.compatibility ,
            'sourcing': user.sourcing,
            'status': user.status,
            
      }
    
  def all_serialize(self,user=None):
    user = user or self.user
    return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'compatibility':user.compatibility ,
            'sourcing': user.sourcing,
            'status': user.status,
            'filename': self.filename
      } 
    
  def request_serialize(self,user=None):
    user = user or self.user
    return {
            'name': user['name'],
            'email': user['email'],
            'compatibility':user['compatibility'] ,
            'sourcing': user['sourcing'],
            'status': user['status']
      } 
    
  def _core_error_serialize(self, error, status):
        return {
            'status': status,
            'description': status.phrase,
            'message': error.message,
        }
    