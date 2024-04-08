from openai import OpenAI

project_id = "proj_OZJBmzM0LDxPS1LDwRmR7n4i"
organization_id = "org-xM2MvxbbXQiBC4DTtiXpryKx"
api_key = "sk-proj-tzA3XMntJe4lZZXd2fJ2T3BlbkFJYGAXgF3J1Qj805wf82Q1"

ClientAI = OpenAI(
  organization=organization_id,
  project=project_id,
  api_key=api_key
)
