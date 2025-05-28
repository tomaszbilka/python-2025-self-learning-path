Tydzień 3: Programowanie obiektowe w Pythonie
✅ Zadanie: Stwórz model systemu rezerwacji (np. bilety, wydarzenia) z wykorzystaniem klas, dziedziczenia i metod specjalnych.

🔹 Kroki:

Zdefiniuj klasę bazową i klasy dziedziczące z odpowiednimi atrybutami i metodami.
Dodaj metody klasowe (@classmethod) i statyczne (@staticmethod).
Zaimplementuj metody magiczne (**str**, **repr**, **eq**, **len** itd.).
Przetestuj tworzenie i działanie obiektów, wykorzystaj dziedziczenie i polimorfizm.

🧱 Struktura:
Entity (bazowa klasa)
│
├── Event
├── User
├── Ticket
│ └── VIPTicket / StandardTicket (dziedziczące po Ticket)
└── Reservation
