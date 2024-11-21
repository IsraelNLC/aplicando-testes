import os
from behave import given, when, then

@given('o workflow chama "{filename}"')
def step_given_workflow_file(context, filename):
    context.filename = filename
    assert os.path.exists(filename), f"Arquivo {filename} não encontrado."

@when('o pipeline é configurado para ser acionado em "{branch}"')
def step_when_pipeline_triggered(context, branch):
    with open(context.filename, "r") as file:
        context.workflow_content = file.read()
    context.branch = branch

@then('o arquivo deve conter "on: push: branches: [{branch}]"')
def step_then_check_branch(context, branch):
    expected = f"on: push: branches: [{branch}]"
    assert expected in context.workflow_content, f"Configuração esperada não encontrada: {expected}"

@when('o pipeline possui um job "{job}"')
def step_when_pipeline_job(context, job):
    context.job = job

@then('o arquivo deve conter "jobs: {job}:"')
def step_then_check_job(context, job):
    expected = f"jobs:\n  {job}:"
    assert expected in context.workflow_content, f"Job esperado não encontrado: {expected}"
