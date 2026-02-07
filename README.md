# Padrões de Projeto em Python

Um repositório sobre padrões de projeto (Design Patterns) implementados em Python.

## 📚 Conteúdo

### 1-Singleton
- **Singleton Pattern** - `1-Singleton/`
  - Garantir uma única instância de uma classe
  - Variações de implementação incluindo thread-safety

### 2-di-lazy-loading-proxy

- **Dependency Injection (DI)** - `2-di-lazy-loading-proxy/di/`
  - Exemplos de injeção de dependência para desacoplamento de código
  
- **Lazy Loading** - `2-di-lazy-loading-proxy/lazy_loading/`
  - Carregamento tardio de recursos para otimização de performance
  
- **Proxy** - `2-di-lazy-loading-proxy/proxy/`
  - Padrão proxy para controle de acesso e operações adicionais

### 3-factory-method-simple-factory-registry

- **Factory Method** - `3-factory-method-simple-factory-registry/factory*.py`
  - Criação de objetos sem especificar suas classes concretas
  
- **Simple Factory** - `3-factory-method-simple-factory-registry/exercicio_simple_factory.py`
  - Padrão simples para criação de instâncias
  
- **Registry Pattern** - `3-factory-method-simple-factory-registry/exercicio_registry.py`
  - Registro centralizado de tipos para criação dinâmica

### 4-decoradores

- **Decoradores** - `4-decoradores/`
  - Decoradores Python para estender funcionalidade
  - Exercícios incluem cache, timer e type checker

### 5-strategy-template-method

- **Strategy** - `5-strategy-template-method/strategy*.py`
  - Encapsulamento de algoritmos intercambiáveis
  
- **Template Method** - `5-strategy-template-method/template_method*.py`
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
python 1-Singleton/singleton1_1.py
python 2-di-lazy-loading-proxy/di/di_1.py
python 3-factory-method-simple-factory-registry/factory1_1.py
python 4-decoradores/decorators1_1.py
python 5-strategy-template-method/strategy1_1.py
```