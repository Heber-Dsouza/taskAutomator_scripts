## `xdotool`

### Site oficial

[xdotool Official Site](https://www.semicomplete.com/projects/xdotool/?utm_source=chatgpt.com)

### GitHub

[xdotool GitHub](https://github.com/jordansissel/xdotool?utm_source=chatgpt.com)

### Manual completo (`man`)

[xdotool man page](https://manpages.ubuntu.com/manpages/latest/man1/xdotool.1.html?utm_source=chatgpt.com)

---

## Comandos mais importantes do `xdotool`

| Ação           | Comando           |
| -------------- | ----------------- |
| Janela ativa   | `getactivewindow` |
| Nome da janela | `getwindowname`   |
| Buscar janela  | `search --name`   |
| Focar janela   | `windowactivate`  |
| Mover janela   | `windowmove`      |
| Redimensionar  | `windowsize`      |
| Minimizar      | `windowminimize`  |
| Mouse          | `mousemove`       |
| Clique         | `click`           |
| Teclas         | `key`             |
| Digitar texto  | `type`            |

---

# `ewmh`

### PyPI

[EWMH PyPI](https://pypi.org/project/EWMH/?utm_source=chatgpt.com)

### GitHub

[EWMH GitHub](https://github.com/parkouss/pyewmh?utm_source=chatgpt.com)

---

## Dependência principal

### `python-xlib`

[python-xlib GitHub](https://github.com/python-xlib/python-xlib?utm_source=chatgpt.com)

### Documentação

[python-xlib Documentation](https://python-xlib.readthedocs.io/en/latest/?utm_source=chatgpt.com)

---

# Métodos principais do `ewmh`

| Método                  | Função                 |
| ----------------------- | ---------------------- |
| `getActiveWindow()`     | janela ativa           |
| `getClientList()`       | listar janelas         |
| `setActiveWindow()`     | focar janela           |
| `setMoveResizeWindow()` | mover/redimensionar    |
| `getWmName()`           | nome da janela         |
| `getDesktopCount()`     | quantidade de desktops |
| `setCurrentDesktop()`   | trocar workspace       |

---

## Exemplo oficial básico

```python id="fw6ewf"
from ewmh import EWMH

ewmh = EWMH()

window = ewmh.getActiveWindow()

print(window.get_wm_name())
```

---

## Diferença arquitetural

| Ferramenta    | Tipo                |
| ------------- | ------------------- |
| `xdotool`     | programa CLI        |
| `ewmh`        | wrapper Python      |
| `python-xlib` | acesso bruto ao X11 |

---

## Quando usar cada um

| Situação              | Melhor                 |
| --------------------- | ---------------------- |
| Script rápido         | `xdotool`              |
| Projeto Python limpo  | `ewmh`                 |
| Controle X11 avançado | `python-xlib`          |
| Automação visual      | `pyautogui` + `opencv` |
