import random

def play_guessing_game():
    """数字当てゲーム - Number guessing game"""
    
    print("=" * 50)
    print("🎮 数字当てゲームへようこそ！")
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    print()
    
    # ゲーム統計
    total_games = 0
    total_attempts = 0
    
    while True:
        # ランダムに1～100の数字を生成
        secret_number = random.randint(1, 100)
        attempts = 0
        guessed = False
        
        print(f"\n🎯 新しいゲームを開始します。1～100の数字を当ててください。")
        print("New game started. Guess a number between 1 and 100.")
        print()
        
        # ゲームループ
        while not guessed:
            try:
                # プレイヤーの入力
                guess = int(input("➜ あなたの予想: "))
                attempts += 1
                
                # 入力値の確認
                if guess < 1 or guess > 100:
                    print("⚠️  1～100の数字を入力してください。")
                    print("   (Please enter a number between 1 and 100)")
                    attempts -= 1
                    continue
                
                # 結果判定
                if guess < secret_number:
                    print(f"📈 もっと大きい数字です！ (Too low!) - 試行回数: {attempts}回")
                elif guess > secret_number:
                    print(f"📉 もっと小さい数字です！ (Too high!) - 試行回数: {attempts}回")
                else:
                    # 正解！
                    guessed = True
                    print()
                    print("🎉 " + "=" * 40)
                    print("🎊 恭喜通過！おめでとうございます！")
                    print("   Congratulations! You got it right!")
                    print("=" * 40)
                    print(f"✨ 正解の数字: {secret_number}")
                    print(f"   Correct number: {secret_number}")
                    print(f"✨ 試行回数: {attempts}回")
                    print(f"   Attempts: {attempts}")
                    print("=" * 40)
                    print()
                    
                    # 統計更新
                    total_games += 1
                    total_attempts += attempts
                    
            except ValueError:
                print("⚠️  数字を入力してください。(Please enter a valid number)")
                continue
        
        # 続行確認
        while True:
            replay = input("\n▶️  もう一度プレイしますか？ (Play again? (y/n)): ").strip().lower()
            if replay in ['y', 'yes', 'はい']:
                break
            elif replay in ['n', 'no', 'いいえ']:
                # ゲーム終了時の統計
                print()
                print("=" * 50)
                print("📊 ゲーム統計 (Game Statistics)")
                print("=" * 50)
                print(f"🎮 プレイしたゲーム数: {total_games}回")
                print(f"   Total games played: {total_games}")
                if total_games > 0:
                    avg_attempts = total_attempts / total_games
                    print(f"📈 平均試行回数: {avg_attempts:.2f}回")
                    print(f"   Average attempts: {avg_attempts:.2f}")
                print("=" * 50)
                print()
                print("🙏 プレイしてくれてありがとうございました！")
                print("   Thank you for playing!")
                return
            else:
                print("⚠️  'y' または 'n' で答えてください。")
                print("   (Please answer with 'y' or 'n')")

if __name__ == "__main__":
    play_guessing_game()
