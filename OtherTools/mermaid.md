# Mermaid Tutorial

## Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    participant Client
    participant OAuthProvider
    participant Server
    Client ->>OAuthProvider: Request access token
    activate OAuthProvider
    OAuthProvider->>Client: Send access token
    deactivate OAuthProvider
    Client->>Server: Request resource
    activate Server
    Server->>OAuthProvider: Validate token
    activate OAuthProvider
    OAuthProvider->>Server: Token valid
    deactivate OAuthProvider
    Server->>Client: Send resource
    deactivate Server
```

## Flow Chart

```mermaid
flowchart LR
    S[Start] --> A;
    A(Enter your email address) --> 
    B{Existing user?};
    B -->|No| C(Enter name)
    C --> D{Accept conditions?}
    D -->|No| A
    D -->|Yes| E(Send email with magic link)
    B -->|Yes| E
```

## Class Diagram

```mermaid
classDiagram
    class Order {
        +OrderStatus status
    }
    class OrderStatus {
        <<enumeration>>
        FAILED
        PENDING
        PAID
    }
    class PaymentProcess {
        <<interface>>
        -String apiKey
        #connect(String url, JSON header)
        +processPayment(Order order) OrderStatus
    }
    class Customer {
        +String name
    }
    Customer <|-- PrivateCustomer
    Customer <|-- BusinessCustomer
    PaymentProcessor <|-- StripePaymentProcessor
    Order o-- Customer
    Car *-- Engine
```

## Entity Relationship Diagram

```mermaid
erDiagram
    Customer ||--o{ Order : places
    Order ||--|{ LineItem : contains
    Customer {
        String id
        String name
    }
    Order {
        String id
        OrderStatus status
    }
    LineItem {
        String code
        String description
        int quantity
        int price
    }
```

## Node

```mermaid
    flowchart LR
        id
```

```mermaid
    flowchart LR
        idA["Heart Suit: &hearts;"]
        idB["Heavy Black Heart: #10084;"]
        idC["Copyright symbol: &copy;"]
```

Direction
- TB, TD, BT, RL, LR
- (round edge)
- ([statium-shaped])
- [[subroutine shaped]]
- [(database shaped)]
- ((circle node))
- >sasymmetric node]
- {rhomubs}

## Shapes

```mermaid
    flowchart LR
        id1(round edge)
        id2([stadium-shaped])
        id3[[subroutine]]
        id4[(Database)]
        id5((circle))
        id6>asymmetric]
        id7{rhombus}
        id8{{hexagon}}
        id9[/parallelogram/]
        id10[\parallelogram\]
        a1[/trapezoid\]
        a2[\trapezoid/]
        a3(((double cicle)))
```

```mermaid
    flowchart RL
        A@{ shape: manual-file, label: "File Handling"}
        B@{ shape: manual-input, label: "User Input"}
        C@{ shape: docs, label: "Multiple Documents"}
        D@{ shape: procs, label: "Process Automation"}
        E@{ shape: paper-tape, label: "Paper Records"}

```

## Gantt

```mermaid
gantt
    title A Gantt Diagram
    dateFormat YYYY-MM-DD
    section Section
        A task          :a1, 2014-01-01, 30d
        Another task    :after a1, 20d
    section Another
        Task in Another :2014-01-12, 12d
        another task    :24d

```

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title       Adding GANTT diagram functionality to mermaid
    excludes    weekends
    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section A section
    Completed task            :done,    des1, 2014-01-06,2014-01-08
    Active task               :active,  des2, 2014-01-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d

    section Critical tasks
    Completed task in the critical line :crit, done, 2014-01-06,24h
    Implement parser and jison          :crit, done, after des1, 2d
    Create tests for parser             :crit, active, 3d
    Future task in critical line        :crit, 5d
    Create tests for renderer           :2d
    Add to mermaid                      :until isadded
    Functionality added                 :milestone, isadded, 2014-01-25, 0d

    section Documentation
    Describe gantt syntax               :active, a1, after des1, 3d
    Add gantt diagram to demo page      :after a1  , 20h
    Add another diagram to demo page    :doc1, after a1  , 48h

    section Last section
    Describe gantt syntax               :after doc1, 3d
    Add gantt diagram to demo page      :20h
    Add another diagram to demo page    :48h

```


## Pie Chart

```mermaid
---
config:
  pie:
    textPosition: 0.5
  themeVariables:
    pieOuterStrokeWidth: "5px"
---
pie showData
    title Key elements in Product X
    "Calcium" : 42.96
    "Potassium" : 50.05
    "Magnesium" : 10.01
    "Iron" :  5

```

## Mindmap

```mermaid
mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectiveness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid

```

## Timeline

```mermaid
timeline
    title History of Social Media Platform
    2002 : LinkedIn
    2004 : Facebook : Google
    2005 : YouTube
    2006 : Twitter

```

```mermaid
timeline
    title Timeline of Industrial Revolution
    section 17th-20th century
        Industry 1.0 : Machinery, Water power, Steam <br>power
        Industry 2.0 : Electricity, Internal combustion engine, Mass production
        Industry 3.0 : Electronics, Computers, Automation
    section 21st century
        Industry 4.0 : Internet, Robotics, Internet of Things
        Industry 5.0 : Artificial intelligence, Big data, 3D printing

```