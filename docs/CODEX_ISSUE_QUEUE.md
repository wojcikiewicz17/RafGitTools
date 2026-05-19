# CODEX Issue Queue (V00–V12)

> Fonte: fila consolidada por Rafael para execução em PRs pequenos, com foco em evidência e rastreabilidade.

## V00 — Protocolo Codex: corrigir por evidência

**Objetivo:** definir a regra operacional.

**Tarefas:**
- ler antes de editar;
- listar arquivos inspecionados;
- não inventar implementação;
- não inventar benchmark;
- não declarar feature pronta sem código + teste;
- separar `implementado`, `parcial`, `stub`, `planejado`.

**Critério de aceite:**
- PR informa arquivos alterados;
- comandos executados;
- resultado real;
- limitações restantes.

---

## V01 — Alinhar README, STATUS_REPORT e FEATURE_MATRIX

**Arquivos:**
- `README.md`
- `docs/STATUS_REPORT.md`
- `docs/FEATURE_MATRIX.md`
- `docs/ROADMAP.md`

**Tarefas:**
- rebaixar linguagem promocional;
- marcar Terminal, IA, DevOps, Enterprise e multiplataforma como roadmap/stub quando não houver código validado;
- manter GitHub + JGit como escopo real atual.

**Critério:**
- documentação não promete produto final sem evidência.

---

## V02 — Criar TESTING_GUIDE.md

**Arquivos:**
- `docs/TESTING_GUIDE.md`
- `app/src/test/`
- `.github/workflows/`

**Tarefas:**
- documentar comandos Gradle reais;
- separar unit, integration, UI e E2E;
- definir metas progressivas: 15%, 25%, 40%, 80%;
- não declarar cobertura nova sem relatório.

---

## V03 — Testes críticos do Git core/JGit

**Arquivos:**
- `JGitService.kt`
- `domain/usecase/git/`
- `app/src/test/`

**Tarefas:**
- testar status;
- testar histórico;
- testar branch básica;
- testar commit básico;
- testar erro de caminho inválido.

**Fora de escopo:**
- LFS;
- GPG;
- GitLab;
- Gitea;
- Bitbucket.

---

## V04 — Testes críticos da GitHub API

**Arquivos:**
- `GithubApiService.kt`
- `GithubRepository.kt`
- `app/src/test/`

**Tarefas:**
- mockar respostas;
- cobrir sucesso e erro HTTP;
- não chamar GitHub real nos testes;
- testar apenas endpoints existentes.

---

## V05 — Criar API_INTEGRATION_GUIDE.md

**Arquivos:**
- `docs/API_INTEGRATION_GUIDE.md`

**Tarefas:**
- documentar GitHub API atual;
- listar endpoints reais;
- separar o que é futuro: GitLab, Bitbucket, Gitea, Azure, webhooks, Enterprise.

---

## V06 — Criar JGIT_OPERATIONS_GUIDE.md

**Arquivos:**
- `docs/JGIT_OPERATIONS_GUIDE.md`
- `JGitService.kt`
- `domain/usecase/git/`

**Tarefas:**
- mapear métodos Git reais;
- separar implementado/parcial/stub;
- não inventar API que não existe.

---

## V07 — Intake dos pacotes RAFAELIA/bench/bare-metal

**Arquivos:**
- `docs/validation/RAFAELIA_BENCH_INTAKE.md`

**Tarefas:**
- registrar pacotes externos;
- separar: compila host, exige NDK, exige avr-gcc, exige hardware, falhou;
- registrar que `bench rafa.zip` veio com `FAIL`, `size=0`, `sha=n/a`, F1..F4 zerados;
- registrar que os 56 métodos C precisam de `-D_POSIX_C_SOURCE=200809L`.

---

## V08 — Criar contrato F1..F4 de benchmark

**Arquivo:**
- `docs/validation/BENCHMARK_CONTRACT.md`

**Tarefas:**
- F1 = cobertura ABI;
- F2 = integridade de artefato;
- F3 = estabilidade temporal real;
- F4 = consistência de grafo;
- exigir CSV/JSON com runs, média, sigma, p95, min, max, timeout, status, sha256, size, arch, compiler e flags.

---

## V09 — Plano de Benchmark Report Viewer

**Arquivo:**
- `docs/validation/BENCHMARK_VIEWER_PLAN.md`

**Tarefas:**
- planejar tela para abrir CSV/JSON;
- estados: `PASS`, `FAIL`, `INCOMPLETE`, `NOT_VALIDATED`;
- fora de escopo: executar benchmark dentro do app.

---

## V10 — Classificar GaiaPhi como experimento

**Arquivo:**
- `docs/validation/GAIAPHI_EXPERIMENT_NOTES.md`

**Tarefas:**
- marcar GaiaPhi como experimento Bash/OpenSSL/HTTP raw;
- registrar limitações: JSON frágil, API key exposta, timeout fraco, dependência de Bash/OpenSSL;
- não integrar no app ainda.

---

## V11 — CI mínimo: build e testes

**Arquivos:**
- `.github/workflows/`
- `docs/TESTING_GUIDE.md`

**Tarefas:**
- inspecionar workflows existentes;
- rodar build Gradle;
- rodar unit tests;
- não publicar badge de cobertura sem relatório real.

---

## V12 — Fechamento da primeira janela

**Arquivos:**
- `docs/STATUS_REPORT.md`
- `docs/ROADMAP.md`
- `docs/validation/`

**Tarefas:**
- consolidar o estado pós-correções;
- listar testes adicionados;
- listar documentação criada;
- listar o que continua parcial/stub;
- sugerir próximas issues só com base em evidência nova.

---

## F de resolvido

A fila está pronta, enumerada e sem invenção. Também foi confirmado que o bloqueio original não era permissão individual: o repositório estava com Issues desativadas (`status: 410`).

## F de gap

Não foi possível gravar via conector naquele momento por dois bloqueios: Issues desativadas e criação de arquivo bloqueada pela ferramenta.

## F de next

1. Ativar **Issues** no repositório e abrir V00–V12 diretamente no GitHub.
2. Manter esta fila em `docs/CODEX_ISSUE_QUEUE.md` como fallback de governança.
3. Executar por PRs pequenos por vértice, sempre com evidência de código/teste.
