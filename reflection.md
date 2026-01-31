# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first opened the game, it worked but there were many bugs. the first bug that I found was that when I was in easy mode, the secret number was 96 when it is supposed to be between 1-20. The second bug I found is that when I guessed a number, it would give a hint saying lower, when the number was higher. The third bug I found was that after a game was finished, the start a new game button would not work.

---

## 2. How did you use AI as a teammate?

I used Copilot's angent in vs code. It helped me provide inline code explanations and helped with refactoring. One suggestion I accepted was fixing the inverted hint logic. One suggestion that I had to deny was copilots initial suggestions for the new game reset. Copilot initially suggested just changing attempts = 0 to attempts = 1. But we also needed to reset the score, status, and history to fully fix the bug.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed by running the game multiple times and checking if the specific problem still happened. One test I ran was playing on Easy mode and verifying the secret number was between 1-20, and testing that hints now said "Go HIGHER!" when my guess was too low instead of saying "Go LOWER!" I also ran pytest tests that Copilot helped generate to verify the `check_guess` function returned correct outcomes and messages for different guess scenarios. AI helped me identify what to test by pointing out the type-switching bug and suggesting I test all three difficulty levels to ensure the range worked correctly.
---

## 4. What did you learn about Streamlit and state?

The secret number wasn't actually changing during gameplay - the real bug was that on even attempts, the code converted the secret to a string which broke the comparison logic. Streamlit reruns your entire script every time you interact with buttons, and session state is like memory that keeps values from resetting between reruns. The fixes I made were removing the type-switching bug, fixing the inverted hints, and making the new game button properly reset all the session state variables (attempts, score, status, history) so you could play multiple rounds.


---

## 5. Looking ahead: your developer habits

One habit I want to reuse is using the debug expander to see what's actually happening with variables like the secret number and game state, because it helped me understand the bugs much faster than just guessing. Next time I work with AI on coding, I would test the code more thoroughly before assuming it works, since the AI-generated game looked fine at first but had multiple hidden bugs. This project showed me that AI can write code that runs without errors but still has logic bugs, so I need to think critically about whether the code actually does what it's supposed to do, not just whether it runs.