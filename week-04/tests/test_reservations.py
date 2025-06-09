import pytest
from main import Reservation, Event, User, StandardTicket
from datetime import datetime

@pytest.fixture
def sample_event():
    return Event("Python Conf 2025", datetime(2025, 9, 15), "Warszawa", capacity=100)

@pytest.fixture
def sample_ticket(sample_event):
    return StandardTicket(sample_event, 100.0)

@pytest.fixture
def sample_user():
    return User("John Doe")

def test_event_inheritance(sample_event):
    assert isinstance(sample_event, Event)
    
def test_event_add_ticket(sample_event, sample_ticket):
    result = sample_event.add_ticket(sample_ticket)
    assert result is True
    assert len(sample_event.tickets) == 1
    assert sample_event.capacity == 100
    
def test_reservation_creation(sample_user, sample_ticket):
    result = Reservation(sample_user, sample_ticket)
    assert result.user == sample_user
    assert result.ticket == sample_ticket
    assert result.ticket.is_reserved is True
    
