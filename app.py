import streamlit as st

from game import check_winner, make_move
from ai import find_move


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Tic-Tac-Toe AI",
    page_icon="🎮",
    layout="centered"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.block-container {
    max-width: 650px;
    padding-top: 2rem;
}

/* Main title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 25px;
}

/* Status */
.game-status {
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    margin: 20px 0;
}

/* Board buttons */
div.stButton > button {
    height: 110px;
    width: 100%;
    font-size: 42px;
    font-weight: bold;
    border-radius: 15px;
    border: 2px solid rgba(128,128,128,0.4);
    transition: 0.2s;
}

div.stButton > button:hover {
    transform: scale(1.03);
}

/* Scoreboard */
[data-testid="stMetric"] {
    text-align: center;
}

/* Center new game button */
.new-game {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# TITLE
# ==========================================

st.markdown(
    '<div class="title">🎮 Tic-Tac-Toe AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Challenge the AI powered by the Minimax algorithm'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# SESSION STATE
# ==========================================

if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "message" not in st.session_state:
    st.session_state.message = "Your turn! ❌"

if "human_score" not in st.session_state:
    st.session_state.human_score = 0

if "ai_score" not in st.session_state:
    st.session_state.ai_score = 0

if "draw_score" not in st.session_state:
    st.session_state.draw_score = 0


# ==========================================
# RESET GAME
# ==========================================

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.game_over = False
    st.session_state.message = "Your turn! ❌"


# ==========================================
# DIFFICULTY
# ==========================================

difficulty = st.selectbox(
    "🎚️ Difficulty",
    ["Easy", "Medium", "Hard"]
)


# ==========================================
# SCOREBOARD
# ==========================================

st.subheader("🏆 Scoreboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "You ❌",
        st.session_state.human_score
    )

with col2:
    st.metric(
        "AI ⭕",
        st.session_state.ai_score
    )

with col3:
    st.metric(
        "Draw 🤝",
        st.session_state.draw_score
    )


# ==========================================
# STATUS
# ==========================================

st.markdown(
    f'<div class="game-status">'
    f'{st.session_state.message}'
    f'</div>',
    unsafe_allow_html=True
)


# ==========================================
# NEW GAME
# ==========================================

if st.button(
    "🔄 New Game",
    use_container_width=True
):
    reset_game()
    st.rerun()


# ==========================================
# GAME BOARD
# ==========================================

for row in range(3):

    cols = st.columns(3, gap="small")

    for col in range(3):

        position = row * 3 + col

        value = st.session_state.board[position]

        if value == "X":
            symbol = "❌"

        elif value == "O":
            symbol = "⭕"

        else:
            symbol = "⬜"

        if cols[col].button(
            symbol,
            key=f"cell_{position}",
            use_container_width=True
        ):

            if (
                not st.session_state.game_over
                and st.session_state.board[position] == ""
            ):

                # --------------------------
                # HUMAN MOVE
                # --------------------------

                make_move(
                    st.session_state.board,
                    position,
                    "X"
                )

                result = check_winner(
                    st.session_state.board
                )

                # Human wins
                if result == "X":

                    st.session_state.message = (
                        "🎉 You won!"
                    )

                    st.session_state.human_score += 1
                    st.session_state.game_over = True

                # Draw
                elif result == "Draw":

                    st.session_state.message = (
                        "🤝 It's a draw!"
                    )

                    st.session_state.draw_score += 1
                    st.session_state.game_over = True

                else:

                    # --------------------------
                    # AI MOVE
                    # --------------------------

                    ai_move = find_move(
                        st.session_state.board,
                        difficulty
                    )

                    if ai_move is not None:

                        make_move(
                            st.session_state.board,
                            ai_move,
                            "O"
                        )

                    result = check_winner(
                        st.session_state.board
                    )

                    # AI wins
                    if result == "O":

                        st.session_state.message = (
                            "🤖 AI wins! Try again!"
                        )

                        st.session_state.ai_score += 1
                        st.session_state.game_over = True

                    # Draw
                    elif result == "Draw":

                        st.session_state.message = (
                            "🤝 It's a draw!"
                        )

                        st.session_state.draw_score += 1
                        st.session_state.game_over = True

                    else:

                        st.session_state.message = (
                            "Your turn! ❌"
                        )

                st.rerun()


# ==========================================
# HOW AI WORKS
# ==========================================

st.divider()

st.subheader("🧠 How the AI Works")

st.write("""
The AI uses the **Minimax algorithm** to evaluate possible
moves and select the best decision.

- 🟢 **Easy** — Random moves
- 🟡 **Medium** — Intelligent + random moves
- 🔴 **Hard** — Optimal Minimax strategy
""")


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Built with Python 🐍 • Streamlit • Minimax AI"
)