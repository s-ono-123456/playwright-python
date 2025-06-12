# 必要なライブラリをインポート
from playwright.sync_api import sync_playwright
import os

# スクリーンショットを保存するディレクトリを作成
screenshot_dir = "screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

# Playwrightを使ってGoogleを開き、スクリーンショットを保存
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.google.com")
    # スクリーンショットを保存
    screenshot_path = os.path.join(screenshot_dir, "google.png")
    page.screenshot(path=screenshot_path)
    print(f"スクリーンショットを保存しました: {screenshot_path}")
    browser.close()
