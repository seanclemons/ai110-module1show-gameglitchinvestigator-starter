import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Tests for bug: "Logic breaks here - hints are inverted"
def test_too_high_message_corrected():
    """Test that 'Too High' now says 'Go LOWER!' (was inverted)"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_too_low_message_corrected():
    """Test that 'Too Low' now says 'Go HIGHER!' (was inverted)"""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_win_message_format():
    """Test that winning message is formatted correctly"""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


# Tests for bug: "New game ignores difficulty range"
def test_easy_difficulty_range():
    """Test that Easy difficulty returns 1-20 range"""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_difficulty_range():
    """Test that Normal difficulty returns 1-100 range"""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_difficulty_range():
    """Test that Hard difficulty returns 1-50 range"""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_unknown_difficulty_defaults():
    """Test that unknown difficulty defaults to 1-100"""
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100
