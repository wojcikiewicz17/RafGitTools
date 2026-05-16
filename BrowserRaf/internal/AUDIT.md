# AUDIT BrowserRaf/internal

## Correções aplicadas
- `_start` em `br_start.S` não chama mais `_start`; agora chama `browser_main`.
- `br_main.c` mudou entrypoint C para `browser_main` para evitar colisão de símbolo.
- `usize` corrigido para 64-bit em ARM64/x86_64.
- `AT_FDCWD` removido como símbolo externo; usa valor syscall `-100` em ARM64 openat.
- Fallback HTTPS→HTTP agora recalcula `sa.port_be` após trocar para porta 80.
- Loops de retry DNS/TCP não fazem chamada extra fora do laço.
- `Makefile` usa `br_start.S + br_main.c` em host ARM64/x86_64 e ARM32, unificando modelo de entrada.

## Pendências conhecidas
- TLS ainda é esqueleto (sem X25519/HKDF/AEAD/cert verify).
- DNS ainda sem timeout de socket.
- HTTP ainda sem chunked/gzip/redirect.
- Render HTML ainda não ignora conteúdo de script/style até tag de fechamento.
