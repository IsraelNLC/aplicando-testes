Feature: Verificar configurações do pipeline do GitHub Actions

  Scenario: Pipeline configurado para branch principal
    Given o workflow chama "deploy.yml"
    When o pipeline é configurado para ser acionado em "main"
    Then o arquivo deve conter "on: push: branches: [main]"

  Scenario: Pipeline com jobs configurados
    Given o workflow chama "deploy.yml"
    When o pipeline possui um job "build"
    Then o arquivo deve conter "jobs: build:"
