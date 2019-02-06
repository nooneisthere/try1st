graph TD;
    A-->B;
    A-->C;
    B-->;
    C-->D;
    

> UML

```
@startuml

actor Client
participant "Websocket" as A
participant "RPC" as B
participant "BOM" as C
participant "Transaction" as D
participant "Quant::Framework" as E
participant "Database" as F
participant "Feed/Redis" as G
participant "bom-market" as H

Client -> A: Persistent connection
activate A

Client -> A: Send request

A -> A: handle itself

group ContractRelated
    Client -> A: Send request

    A -> B: Client request (contract)
    activate B

    B --> C: Contract related
    activate C

    C --> B: Contract response
    deactivate C

    B -> A: RPC response
    destroy B

    A -> Client: Send response
end

group Transaction
    Client -> A: Send request (buy/sell)

    A -> B : Client request (buy/sell)
    activate B

    B --> D: Buy/sell
    activate D

    D --> F: perform operation
    F --> D: Success/failure

    D --> B: Buy/sell response
    deactivate D

    B -> A: RPC response
    destroy B
end

group MarketRelated
    Client -> A: Get active_symbols

    A -> B: Client request (active_symbols)
    activate B

    B --> E: Get all market symbols
    activate E

    E --> B: Symbols response
    deactivate E

    B -> A: RPC response
    destroy B
end

group Streaming
    Client -> A: Subscribe to ticks

    A -> B: Initial RPC call (validations etc)
    activate B

    B --> H: Validations
    activate H

    H --> B
    destroy H

    B -> A: Initial response
    destroy B

    A -> Client: Send initial response

    A -> G: Subscribe
    activate G

    G -> G: Update/Receive new tick

    G -> A: Publish
    deactivate G

    A -> Client: Send response
end

@enduml
```
