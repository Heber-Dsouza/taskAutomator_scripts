```python
import uuid

from classes.operating_system.application import Application
from classes.core.keyboard import Keyboard

class Calculator(Application):
    global_id = str(uuid.uuid4())
    running_stack:list[str] = []

    def __init__(self):
        super().__init__("gnome-calculator", self.global_id, self.running_stack)
```

**Q:** Toda a vez que crio uma classe que herda de Application, quero algo que indique que é necessário criar as duas props staticas:

`global_id = str(uuid.uuid4())`
`running_stack:list[str] = []`

---

Em Python o mais correto é definir isso na classe pai.

Assim as classes filhas herdam automaticamente e você não precisa repetir.

Exemplo:

```python id="m7q2vx"
import uuid


class Application:
    global_id: str = str(uuid.uuid4())
    running_stack: list[str] = []

    def __init__(
        self,
        launch_command: str
    ):
        self.launch_command = launch_command
```

Agora:

```python id="k4n8rp"
class Calculator(Application):
    def __init__(self):
        super().__init__("gnome-calculator")
```

---

Mas atenção:

```python id="t1q6zp"
running_stack = []
```

na classe pai será compartilhado entre TODAS as subclasses e instâncias.

Se quiser uma lista separada por classe filha, use:

```python id="w5k3mv"
class Application:
    def __init_subclass__(cls):
        cls.global_id = str(uuid.uuid4())
        cls.running_stack = []
```

Agora cada subclasse recebe automaticamente:

```python id="x9r2qa"
class Calculator(Application):
    pass


class Browser(Application):
    pass
```

Cada uma terá:

* `global_id` único
* `running_stack` própria

Sem precisar declarar manualmente.

---

    def __init_subclass__(cls): 

      cls.global_id = str(uuid.uuid4())

      cls.running_stack = []

**Q:** Excelente, qual o equivalente desse recurso no TS?

---

Em TypeScript não existe um equivalente direto de `__init_subclass__`.

O mais próximo normalmente é:

* static fields
* decorators
* factory functions
* metaprogramming

Exemplo parecido usando static props:

```typescript id="m7q2vx"
import { randomUUID } from 'crypto'

class Application {
  static globalId = randomUUID()
  static runningStack: string[] = []
}

class Calculator extends Application {}
```

Mas aqui:

* os valores são herdados
* não são recriados automaticamente por subclasse

Então `Calculator.globalId` seria o mesmo da classe pai.

---

Para gerar automaticamente por subclasse, o equivalente mais próximo seria um decorator:

```typescript id="k4n8rp"
import { randomUUID } from 'crypto'

function ApplicationConfig<T extends Function>(target: T) {
  ;(target as any).globalId = randomUUID()
  ;(target as any).runningStack = []
}

@ApplicationConfig
class Calculator {}
```

---

Ou manualmente:

```typescript id="t1q6zp"
class Calculator extends Application {
  static globalId = randomUUID()
  static runningStack: string[] = []
}
```

Python possui metaprogramação de classes muito mais poderosa e simples que TS nesse ponto.

---

**Q:** E como acessar a prop no restante da classe?

---

Se você usar `__init_subclass__`, em Python as propriedades continuam sendo acessadas normalmente.

Exemplo:

```python id="m7q2vx"
import uuid


class Application:
    def __init_subclass__(cls):
        cls.global_id = str(uuid.uuid4())
        cls.running_stack = []


class Calculator(Application):

    def show_data(self):
        print(self.global_id)
        print(self.running_stack)
```

Uso:

```python id="k4n8rp"
c = Calculator()

c.show_data()
```

---

Também pode acessar pela própria classe:

```python id="t1q6zp"
print(Calculator.global_id)
print(Calculator.running_stack)
```

---

Dentro da classe:

* `self.global_id`
* `self.running_stack`

funcionam normalmente porque Python procura:

1. instância
2. classe
3. herança

automaticamente.

---

