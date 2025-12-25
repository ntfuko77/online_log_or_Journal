from pydantic import BaseModel,Field
from typing import List,Any, Literal,Dict


class Simple_Parameter_properties(BaseModel):
    type: Literal["string", "number", "integer", "boolean", "array", "object"]=Field(...)
    description: str=Field(...)

class Parameters(BaseModel):
    type: Literal["object"] =Field(default="object")
    required: List[str] = Field(...)
    properties:  Dict[str, Simple_Parameter_properties] = Field(...)
    
class Tool(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    parameters: Parameters = Field(...)
    type: Literal["function"] =Field(default="function")
    strict: bool = Field(default=True)
    
class Toollist(BaseModel):
    tools: List[Tool] =[]
    def form_input(self):
        return [tool.model_dump() for tool in self.tools]
class SimpleInput(BaseModel):
    role: Literal["user", "assistant", "developer"] = Field(...)
    content: str = Field(...)
class ResponseInput(BaseModel):
    input: List[SimpleInput] = Field(...)
    tools: List[Tool] = Field(default_factory=list)
    model: str = Field(...)
    instructions: str = Field(default="You are a helpful assistant.")
    
    


