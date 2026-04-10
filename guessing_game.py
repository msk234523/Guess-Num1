import random

# ── ダークテーマ用 ANSI カラーコード ──────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    BG      = "\033[40m"    # 黒背景
    WHITE   = "\033[97m"    # 明るい白
    CYAN    = "\033[96m"    # シアン（低い）
    YELLOW  = "\033[93m"    # 黄（高い）
    GREEN   = "\033[92m"    # 緑（正解）
    RED     = "\033[91m"    # 赤（警告）
    MAGENTA = "\033[95m"    # マゼンタ（統計）
    DIM     = "\033[2m"     # 薄い文字

def _p(color: str, text: str) -> None:
    """ダークテーマで1行出力する"""
    print(f"{C.BG}{color}{text}{C.RESET}")

def _div(char: str = "─", width: int = 50) -> None:
    _p(C.DIM, char * width)


def play_guessing_game():
    """数字当てゲーム - Number guessing game"""

    _div("═")
    _p(C.BOLD + C.WHITE, "  🎮 数字当てゲームへようこそ！")
    _p(C.WHITE,           "     Welcome to the Number Guessing Game!")
    _div("═")
    print()

    # ゲーム統計
    total_games = 0
    total_attempts = 0

    while True:
        # ランダムに1～100の数字を生成
        secret_number = random.randint(1, 100)
        attempts = 0
        guessed = False

        print()
        _p(C.CYAN, "  🎯 新しいゲームを開始します。1～100の数字を当ててください。")
        _p(C.DIM,  "     New game started. Guess a number between 1 and 100.")
        print()

        # ゲームループ
        while not guessed:
            try:
                # プレイヤーの入力
                guess = int(input(f"{C.BG}{C.WHITE}  ➜ あなたの予想: {C.RESET}"))
                attempts += 1

                # 入力値の確認
                if guess < 1 or guess > 100:
                    _p(C.RED, "  ⚠️  1～100の数字を入力してください。")
                    _p(C.DIM, "      (Please enter a number between 1 and 100)")
                    attempts -= 1
                    continue

                # 結果判定
                if guess < secret_number:
                    _p(C.CYAN,   f"  📈 もっと大きい数字です！ (Too low!)  ─ 試行回数: {attempts}回")
                elif guess > secret_number:
                    _p(C.YELLOW, f"  📉 もっと小さい数字です！ (Too high!) ─ 試行回数: {attempts}回")
                else:
                    # 正解！
                    guessed = True
                    print()
                    _div("═")
                    _p(C.BOLD + C.GREEN, "  🎉 おめでとうございます！ Congratulations!")
                    _div("─")
                    _p(C.WHITE, f"  ✨ 正解の数字 / Correct number : {secret_number}")
                    _p(C.WHITE, f"  ✨ 試行回数   / Attempts       : {attempts}回")
                    _div("═")
                    print()

                    # 統計更新
                    total_games += 1
                    total_attempts += attempts

            except ValueError:
                _p(C.RED, "  ⚠️  数字を入力してください。(Please enter a valid number)")
                continue

        # 続行確認
        while True:
            replay = input(
                f"{C.BG}{C.WHITE}  ▶️  もう一度プレイしますか？ (Play again? y/n): {C.RESET}"
            ).strip().lower()
            if replay in ['y', 'yes', 'はい']:
                break
            elif replay in ['n', 'no', 'いいえ']:
                # ゲーム終了時の統計
                print()
                _div("═")
                _p(C.BOLD + C.MAGENTA, "  📊 ゲーム統計 (Game Statistics)")
                _div("─")
                _p(C.WHITE, f"  🎮 プレイしたゲーム数 / Total games  : {total_games}回")
                if total_games > 0:
                    avg = total_attempts / total_games
                    _p(C.WHITE, f"  📈 平均試行回数       / Avg attempts : {avg:.2f}回")
                _div("═")
                print()
                _p(C.CYAN, "  🙏 プレイしてくれてありがとうございました！")
                _p(C.DIM,  "     Thank you for playing!")
                print()
                return
            else:
                _p(C.RED, "  ⚠️  'y' または 'n' で答えてください。(Please answer with 'y' or 'n')")

if __name__ == "__main__":
    play_guessing_game()
