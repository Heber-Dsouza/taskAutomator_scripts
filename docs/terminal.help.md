Ao iniciar um processo com o terminal, esse processo fica vinculado.

Ao fechar o terminal com o processo rodando, o processe será encerrado com o terminal.

Existem algumas formas de solucionar isso:

### Usando o ... &

Ex.:

```bash
gnome-calculator &
```

O terminal fica preso no processo e encerra o processo caso seja fechado

### Usando o nohup ... &

Ex.:

```bash
nohup gnome-calculator &
```

O terminal deixa de ficar preso no processo para poder ser usado,
podendo encerrar o terminal sem encerrar o processo

### Usando o ... & disown

Ex.:

```bash
gnome-calculator & disown
```

O terminal fica preso no processo, mas pode ser fechado sem encerrar o processo


---
### Resumo:

| Método     | Continua após fechar terminal | Controle pelo shell | Output automático |
| ---------- | ----------------------------- | ------------------- | ----------------- |
| `&`        | ❌ não confiável               | sim                 | sim               |
| `nohup &`  | ✔ sim                         | parcial             | gera `nohup.out`  |
| `& disown` | ✔ sim                         | não                 | não               |
