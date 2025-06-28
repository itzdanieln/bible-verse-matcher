import sys
import os

# Add the backend/ directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from ai_engine import match_bible_verse

test_input = "Be still, and know that I am God"
verse = match_bible_verse(test_input)
print("Matched Verse:")
print(verse)