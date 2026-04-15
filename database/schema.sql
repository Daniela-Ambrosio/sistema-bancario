-- tabela de Contas
CREATE TABLE IF NOT EXISTS contas (
    numero_conta INTEGER PRIMARY KEY,
    titular TEXT,
    cpf INTEGER,
    saldo REAL
);

-- tabela de Transações
CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_conta INTEGER,
    operacao TEXT,
    valor REAL,
    data_hora TEXT,
    descricao_criptografada TEXT,
    FOREIGN KEY (numero_conta) REFERENCES contas(numero_conta)
);