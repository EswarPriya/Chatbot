
import json
from .base import BaseModel

class Transcript(BaseModel):

    transcript = ''
    
    def __init__(self):
        BaseModel.__init__(self)

    def add_to_transcript(self,arr):
        self.transcript = arr
