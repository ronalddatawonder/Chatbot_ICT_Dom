import pytest
from chatbot import get_bot_response, initialize_session_state, ict_faqs
import streamlit as st

def test_get_bot_response_exact_match():
    """Test dat een exacte match in de FAQ het juiste antwoord geeft"""
    test_input = "ik ben mijn wachtwoord vergeten"
    expected_response = ict_faqs[test_input]
    assert get_bot_response(test_input) == expected_response

def test_get_bot_response_case_insensitive():
    """Test dat hoofdlettergevoeligheid geen rol speelt"""
    test_input = "IK BEN MIJN WACHTWOORD VERGETEN"
    expected_response = ict_faqs["ik ben mijn wachtwoord vergeten"]
    assert get_bot_response(test_input) == expected_response

def test_get_bot_response_no_match():
    """Test dat een niet-bestaande vraag het juiste standaard antwoord geeft"""
    test_input = "dit staat niet in de FAQ"
    assert "Sorry, ik kon geen direct antwoord vinden" in get_bot_response(test_input)

def test_get_bot_response_whitespace():
    """Test dat extra whitespace wordt genegeerd"""
    test_input = "   ik ben mijn wachtwoord vergeten   "
    expected_response = ict_faqs["ik ben mijn wachtwoord vergeten"]
    assert get_bot_response(test_input) == expected_response

def test_initialize_session_state():
    """Test dat session state correct wordt geïnitialiseerd"""
    # Verwijder chat_history als die al bestaat
    if 'chat_history' in st.session_state:
        del st.session_state.chat_history
    
    # Test initialisatie
    initialize_session_state()
    assert 'chat_history' in st.session_state
    assert isinstance(st.session_state.chat_history, list)
    assert len(st.session_state.chat_history) == 0