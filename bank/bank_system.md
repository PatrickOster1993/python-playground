# Banksystem Architektur

## Klassendiagramm

```mermaid
classDiagram
    class Bank {
        -name: String
        -address: String
        -swiftCode: String
        -logo: String
        -hasOnlineBanking: bool
    }
    
    class Customer {
        -customerID: String
        -name: String
        -address: String
        -accounts: Account[]
    }
    
    class Account {
        -accountNumber: String
        -balance: float
        -type: String
        -owner: Customer
    }

    Bank "1" -- "*" Customer : hat
    Customer "1" -- "*" Account : besitzt
```

## Beschreibung der Komponenten

### Bank
- Repräsentiert das Bankinstitut selbst
- Speichert grundlegende Informationen wie Name, Adresse und SWIFT-Code
- Optional: Online-Banking-Funktionalität

### Customer (Kunde)
- Repräsentiert einen Bankkunden
- Enthält persönliche Informationen
- Aggregiert mehrere Konten

### Account (Konto)
- Repräsentiert ein Bankkonto
- Enthält Kontostand und Kontotyp
- Gehört zu einem Kunden

## Implementierungsstruktur

```
bank/
├── __init__.py
├── bank.py
├── customer.py
└── account.py