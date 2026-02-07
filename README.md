# Padrões de Projeto em Python

Um repositório sobre padrões de projeto (Design Patterns) implementados em Python.

## 📚 Conteúdo

### 1 - Singleton
- **Singleton Pattern** - `singleton/`
  - Garantir uma única instância de uma classe
  - Variações de implementação incluindo thread-safety

### 2 - Injeção de Dependências, Lazy Loading e Proxy

- **Dependency Injection (DI)** - `aula2/di/`
  - Exemplos de injeção de dependência para desacoplamento de código
  
- **Lazy Loading** - `aula2/lazy_loading/`
  - Carregamento tardio de recursos para otimização de performance
  
- **Proxy** - `aula2/proxy/`
  - Padrão proxy para controle de acesso e operações adicionais

### 3 - Factory Method, Simple Factory e Registry

- **Factory Method** - `aula3/factory*_*.py`
  - Criação de objetos sem especificar suas classes concretas
  
- **Simple Factory** - `aula3/exercicio_simple_factory.py`
  - Padrão simples para criação de instâncias
  
- **Registry Pattern** - `aula3/exercicio_registry.py`
  - Registro centralizado de tipos para criação dinâmica

### 4 - Decoradores

- **Decoradores** - `aula4_decoradores/`
  - Decoradores Python para estender funcionalidade
  - Exercícios incluem cache, timer e type checker

### 5 - Strategy e Template Method

- **Strategy** - `aula5/strategy*_*.py`
  - Encapsulamento de algoritmos intercambiáveis
  
- **Template Method** - `aula5/template_method*_*.py`
  - Definição do esqueleto de um algoritmo
  
- **Exemplos adicionais** - Validador, Formatador de Data, Cálculo de Frete


## 🚀 Como Usar

1. Clone o repositório:
```bash
git clone git@github.com:julianofischer/padroesdeprojetoempython.git
cd padroesdeprojetoempython
```

2. Crie um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute os exemplos:
```bash
python aula2/di/di_1.py
python aula3/factory1_1.py
# ... etc
```