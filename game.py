import random

def start_game():
    print("==============================")
    print("   歡迎來到『數字生存挑戰』！")
    print("==============================")
    print("規則：電腦已選定一個 1 到 100 之間的數字。")
    print("你有 10 點體力，每次猜錯會扣除 1 點。")
    print("看看你能不能在體力耗盡前找到答案！\n")

    # 初始化設定
    target_number = random.randint(1, 100)
    health = 10
    attempts = 0

    while health > 0:
        try:
            print(f"目前體力: {'❤️' * health} ({health}/10)")
            guess = int(input("請輸入你猜的數字 (1-100): "))
        except ValueError:
            print("❌ 無效輸入！請輸入一個『數字』。\n")
            continue

        attempts += 1

        # 邏輯判斷
        if guess < 1 or guess > 100:
            print("⚠️ 提醒：數字超出了範圍 (1-100)，浪費了一次體力！")
            health -= 1
        elif guess < target_number:
            print("🔼 太小了！再大一點。")
            health -= 1
        elif guess > target_number:
            print("🔽 太大了！再小一點。")
            health -= 1
        else:
            print(f"\n🎉 恭喜破關！答案就是 {target_number}！")
            print(f"你總共嘗試了 {attempts} 次，剩餘體力 {health}。")
            break

        if health == 0:
            print("\n💀 體力耗盡！你倒下了...")
            print(f"正確答案其實是: {target_number}")

    print("\n遊戲結束，感謝遊玩！")

if __name__ == "__main__":
    start_game()