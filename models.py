from pydantic import BaseModel, field_validator, ValidationError, Field
import os
from pydantic_ai import RunContext
from typing import Optional

active_studies = ['mtm-t2','ABCstudy']

class defaultDeps(BaseModel):
    name : str
    study_name : str

    @field_validator('study_name', mode='before')
    @classmethod
    def confirm_study_name(cls, name):
        if not isinstance(name, str):
            try:
                name = str(name)
            except:
                raise TypeError(f"Expected model_name to be type str, but was {type(name)}")

        name = name.lower()

        if name not in active_studies:
            raise ValidationError("Study name does not match any active studies")
        
        return name

class commitSingleFileToGitHubParams(BaseModel):
    title: str = Field(min_length=10, max_length=100, description="Commit title")
    description: str = Field(min_length=20, max_length=500, description="Description of commit changes")
    path: str = Field(description="Path to the file being comitted")
    repo: str = Field(description="Location of the git repository")

    @field_validator("path")
    @classmethod
    def verify_path(cls, path: str) -> str:
        cleanpath = path.replace('\\', '/').strip()
        try:
            os.access(cleanpath, mode=0)
        except:
            raise ValueError(f"{path} was not found")
        
        return cleanpath

class File(BaseModel):
    path: str
    file_contents: str

class pushToGithubParams(BaseModel):
    branch: str = Field(description="Branch to push to")
    files: list[File] = Field(description = "Array of file objects to push, each object with path (string) and content (string)")
    message: str = Field(description="Commit message")
    owner: str = Field(description="Repository owner")
    repo: str = Field(description="Repository name")

def construct_pushToGithubParams(ctx: RunContext[ghAgentContext], files, message) -> pushToGithubParams:
    return pushToGithubParams(
        branch="main",
        files=files,
        message=message,
        owner = ctx.deps.git_repo_owner_name,
        repo = ctx.deps.git_repository,
    )

class ghAgentContext(BaseModel):
    user_name: str
    git_repository: str
    git_repo_owner_name: str